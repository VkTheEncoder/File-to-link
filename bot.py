import sys
import glob
import importlib
import logging
import logging.config
import pytz
import asyncio
import time
from pathlib import Path
from datetime import date, datetime

from pyrogram import Client, filters, idle
from aiohttp import web

from database.users_chats_db import db
from config import *
from utils import temp
from Script import script
from plugins import web_server

from UHDBots.bot import UHDBots
from UHDBots.util.keepalive import ping_server
from UHDBots.bot.clients import initialize_clients

# ---------------- Logging ----------------
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)

for noisy_logger in ["pyrogram", "imdbpy", "aiohttp", "aiohttp.web"]:
    logging.getLogger(noisy_logger).setLevel(logging.ERROR)

# ---------------- Globals ----------------
START_TIME = time.time()
BANNED_USERS = set()
EMOJI_LIST = ["😎", "🔥", "❤️", "🤖"]  # Auto emoji react

# ---------------- Plugin Loader ----------------
def load_plugins():
    """Dynamically import all plugins from plugins/ folder."""
    ppath = "plugins/*.py"
    files = glob.glob(ppath)
    for name in files:
        plugin_path = Path(name)
        plugin_name = plugin_path.stem
        import_path = f"plugins.{plugin_name}"

        spec = importlib.util.spec_from_file_location(import_path, plugin_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        sys.modules[import_path] = module
        logging.info(f"✅ UHD Bots Imported => {plugin_name}")

# ---------------- Command Handlers ----------------
def add_command_handlers():
    # ===== PING =====
    @UHDBots.on_message(filters.command("ping") & filters.user(ADMINS))
    async def ping_handler(client, message):
        start_t = time.time()
        m = await message.reply_text("🏓 Pinging...")
        end_t = time.time()
        await m.edit_text(f"✅ Pong! `{round((end_t - start_t) * 1000)} ms`")

    # ===== UPTIME =====
    @UHDBots.on_message(filters.command("uptime") & filters.user(ADMINS))
    async def uptime_handler(client, message):
        uptime = time.time() - START_TIME
        days, rem = divmod(int(uptime), 86400)
        hours, rem = divmod(rem, 3600)
        minutes, seconds = divmod(rem, 60)
        await message.reply_text(f"⏱ Uptime: `{days}d {hours}h {minutes}m {seconds}s`")

    # ===== BAN =====
    @UHDBots.on_message(filters.command("ban") & filters.user(ADMINS))
    async def ban_handler(client, message):
        if not message.reply_to_message:
            return await message.reply_text("⚠️ Reply to a user to ban them.")
        user_id = message.reply_to_message.from_user.id
        await db.banned_users.update_one(
            {"user_id": user_id},
            {"$set": {"user_id": user_id, "banned_at": datetime.utcnow()}},
            upsert=True
        )
        await message.reply_text(f"🚫 User `{user_id}` has been banned.")

    # ===== UNBAN =====
    @UHDBots.on_message(filters.command("unban") & filters.user(ADMINS))
    async def unban_handler(client, message):
        if not message.reply_to_message:
            return await message.reply_text("⚠️ Reply to a user to unban them.")
        user_id = message.reply_to_message.from_user.id
        result = await db.banned_users.delete_one({"user_id": user_id})
        if result.deleted_count:
            await message.reply_text(f"✅ User `{user_id}` has been unbanned.")
        else:
            await message.reply_text("⚠️ This user is not banned.")

    # ===== STATS =====
    @UHDBots.on_message(filters.command("stats"))
    async def stats_handler(client, message):
        total_users = await db.users.count_documents({})
        total_chats = await db.chats.count_documents({})
        await message.reply_text(
            f"📊 Bot Statistics:\n\n👤 Total Users: {total_users}\n💬 Total Chats: {total_chats}"
        )

    # ===== AUTO EMOJI REACT =====
    @UHDBots.on_message(filters.group | filters.channel)
    async def auto_emoji_react(client, message):
        import random
        emoji = random.choice(EMOJI_LIST)
        try:
            await message.reply_text(emoji, quote=True)
        except:
            pass

# ---------------- Bot Startup ----------------
async def start():
    print("\n🚀 Initializing UHD Bots...\n")

    await UHDBots.start()
    bot_info = await UHDBots.get_me()

    await initialize_clients()
    load_plugins()

    if ON_HEROKU:
        asyncio.create_task(ping_server())

    temp.BOT = UHDBots
    temp.ME = bot_info.id
    temp.U_NAME = bot_info.username
    temp.B_NAME = bot_info.first_name

    tz = pytz.timezone("Asia/Kolkata")
    today = date.today()
    now = datetime.now(tz)
    time_now = now.strftime("%H:%M:%S %p")

    await UHDBots.send_message(
        chat_id=LOG_CHANNEL,
        text=script.RESTART_TXT.format(today, time_now)
    )

    app = web.AppRunner(await web_server())
    await app.setup()
    await web.TCPSite(app, "0.0.0.0", PORT).start()

    # ✅ Add command handlers
    add_command_handlers()

    await idle()

# ---------------- Run Bot ----------------
if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(start())
    except KeyboardInterrupt:
        logging.info("🛑 Service Stopped. Bye 👋")
