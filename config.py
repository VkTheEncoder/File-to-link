# 🗿  Visit & Support us - @UHD_Official
# ⚡️ Do Not Remove Credit - Made by @UHD_Bots
# 💬 For Any Help Join Support Group: @UHDBots_Support
# 🚫 Removing or Modifying these Lines will Cause the bot to Stop Working.


import re
from os import environ


id_pattern = re.compile(r'^-?\d+$')


SESSION = environ.get("SESSION", "UHDFiletoLinksBot")
API_ID = int(environ.get("API_ID", "25341849"))
API_HASH = environ.get("API_HASH", "c22013816f700253000e3c24a64db3b6")
BOT_TOKEN = environ.get("BOT_TOKEN", "8358372369:AAG10vPmTUDlapCgzlSr_7BFPnLhV4RhWUQ")


PORT = int(environ.get("PORT", "8080"))
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
ON_HEROKU = "DYNO" in environ
URL = environ.get("URL", "")


LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "0"))
ADMINS = [
    int(admin) if id_pattern.match(admin) else admin
    for admin in environ.get("ADMINS", "").split()
]


DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://ripofi9693_db_user:UYyAtNWQtQ5PEfsP@cluster0.j6j5gqy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get("DATABASE_NAME", "File_to_link")
