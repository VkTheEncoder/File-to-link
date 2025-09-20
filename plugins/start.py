import random
import humanize
from Script import script
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import URL, LOG_CHANNEL
from urllib.parse import quote_plus
from UHDBots.util.file_properties import get_name, get_hash, get_media_file_size
from UHDBots.util.human_readable import humanbytes
from database.users_chats_db import db
from utils import temp



@Client.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    await message.reply_text(
        text=(
            "👋 <b>ʜɪɪ,\n\n🗿 ɪ ᴀᴍ ʟᴀᴛᴇsᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ ᴛᴏ ʟɪɴᴋs ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴊᴜsᴛ sᴇɴᴅ ᴀɴʏ ᴍᴇᴅɪᴀ ᴏʀ ғɪʟᴇ ᴛᴏ ɢᴇᴛ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ sᴛʀᴇᴀᴍ ʟɪɴᴋ.\n\n ᴘʟᴇᴀsᴇ ᴜsᴇ & sʜᴀʀᴇ ᴍᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ ᥙs ᴍᴀᴅᴇ ʙʏ ᴜʜᴅ ʙᴏᴛs™</b> 🔥"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/UHD_Bots"),
                    InlineKeyboardButton("💡 ᴄᴏᴅᴇs", url="https://github.com/UHD-Botz/UHD-FiletoLinks-Bot")
                ],
                [
                    InlineKeyboardButton("📜 ᴜʜᴅ ᴏғғɪᴄɪᴀʟ", url="https://t.me/UHD_Official"),
                    InlineKeyboardButton("🌐 ʜᴅ ᴍᴏᴠɪᴇs ᴇᴀʀᴛʜ", url="https://bit.ly/HDMoviesEarth")
                ]
            ]
        ),
        disable_web_page_preview=True,
        quote=True
    )



@Client.on_message(filters.private & (filters.document | filters.video))
async def stream_start(client, message):
    try:
        file = getattr(message, message.media.value)
        filename = file.file_name
        filesize = humanize.naturalsize(file.file_size)
        fileid = file.file_id
        user_id = message.from_user.id
        username = message.from_user.mention

        
        log_msg = await client.send_cached_media(
            chat_id=LOG_CHANNEL,
            file_id=fileid,
        )

        fileName = get_name(log_msg)

        
        stream = f"{URL}watch/{log_msg.id}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"
        download = f"{URL}{log_msg.id}/{quote_plus(get_name(log_msg))}?hash={get_hash(log_msg)}"

        
        await log_msg.reply_text(
            text=f"📌 ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴇᴅ ғᴏʀ ᴜsᴇʀ {username} (ID: {user_id})\n\n"
                 f"📂 ғɪʟᴇ ɴᴀᴍᴇ: {fileName}",
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("🚀 ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ", url=download),
                    InlineKeyboardButton("🖥 ᴡᴀᴛᴄʜ", url=stream)
                ]]
            )
        )

        
        msg_text = (
            "<i><u>✅ ʏᴏᴜʀ ʟɪɴᴋ ɪs ʀᴇᴀᴅʏ!!</u></i>\n\n"
            f"<b>📂 ғɪʟᴇ ɴᴀᴍᴇ:</b> <i>{fileName}</i>\n"
            f"<b>📦 ғɪʟᴇ sɪᴢᴇ:</b> <i>{filesize}</i>\n\n"
            f"<b>📥 ᴅᴏᴡɴʟᴏᴀᴅ:</b> <i>{download}</i>\n\n"
            f"<b>🖥 ᴡᴀᴛᴄʜ:</b> <i>{stream}</i>\n\n"
            "<b>🚸 ɴᴏᴛᴇ:</b> ʟɪɴᴋs ᴡɪʟʟ ᴡᴏʀᴋ ᴜɴᴛɪʟ ɪ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ғɪʟᴇ."
        )

        await message.reply_text(
            text=msg_text,
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton("📥 ғᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ", url=download),
                    InlineKeyboardButton("🖥 ᴡᴀᴛᴄʜ", url=stream)
                ]]
            )
        )

    except Exception as e:
        await message.reply_text(f"⚠️ Error: {str(e)}")
