# 🗿  Visit & Support us - @UHD_Official
# ⚡️ Do Not Remove Credit - Made by @UHD_Bots
# 💬 For Any Help Join Support Group: @UHDBots_Support
# 🚫 Removing or Modifying these Lines will Cause the bot to Stop Working.


import sys
import glob
import importlib
import logging
import logging.config
import pytz
import asyncio
from pathlib import Path
from typing import Union, Optional, AsyncGenerator
from datetime import date, datetime

from pyrogram import Client, idle
from aiohttp import web


from database.users_chats_db import db
from config import *        
from utils import temp
from Script import script
from plugins import web_server


from UHDBots.bot import UHDBots
from UHDBots.util.keepalive import ping_server
from UHDBots.bot.clients import initialize_clients



logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)


for noisy_logger in ["pyrogram", "imdbpy", "aiohttp", "aiohttp.web"]:
    logging.getLogger(noisy_logger).setLevel(logging.ERROR)



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
    time = now.strftime("%H:%M:%S %p")

    await UHDBots.send_message(
        chat_id=LOG_CHANNEL,
        text=script.RESTART_TXT.format(today, time)
    )

    
    app = web.AppRunner(await web_server())
    await app.setup()
    await web.TCPSite(app, "0.0.0.0", PORT).start()

    await idle()



if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(start())
    except KeyboardInterrupt:
        logging.info("🛑 Service Stopped. Bye 👋")


