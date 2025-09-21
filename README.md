<p align="center">
  <img src="https://img.shields.io/github/license/UHD-Botz/UHD-Auto-React-Bot?style=for-the-badge&color=blue" />
  <img src="https://img.shields.io/badge/Made%20By-UHD%20Official-8A2BE2?style=for-the-badge&logo=telegram" />
  <img src="https://img.shields.io/badge/Powered%20By-Pyrogram-2c2c2c?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/MongoDB-Async-brightgreen?style=for-the-badge&logo=mongodb" />
</p>

<h1 align="center">🤖 UHD Auto React Bot</h1>
<p align="center">
  A powerful <b>Telegram Auto Reaction Bot</b> built with <code>Pyrogram</code> + <code>MongoDB</code>, featuring admin controls, stats, force-subscribe, caching & more.  
</p>

---

## ⚙️ Features

| 🚀 Feature             | 🧠 Description                                                                 |
|------------------------|--------------------------------------------------------------------------------|
| 🤖 Auto Emoji React    | Reacts to every message in group/channel with rotating emojis                  |
| 🚫 Ban / Unban         | Block users from using bot using `/ban` & `/unban`                            |
| 📊 Stats Command       | Admin-only: See total number of users in the bot                              |
| 🛠 Restart             | Instantly restart the bot from Telegram with `/restart`                       |
| 🔎 Ping Command        | Test bot latency with `/ping`                                                 |
| 🔐 Force Subscribe     | Optional mandatory channel subscription (`IS_FSUB`)                           |
| ⚡ MongoDB Caching     | AsyncDB with memory cache for faster access                                   |

---

## 🔥 Setup & Deployment

### 🔑 Required Variables
- `BOT_TOKEN` → Get from [@BotFather](https://t.me/BotFather)  
- `API_ID` → From [Telegram API](https://my.telegram.org/apps)  
- `API_HASH` → From [Telegram API](https://my.telegram.org/apps)  
- `ADMIN` → Your Telegram ID (multiple admins separated by space)  
- `DB_URI` → MongoDB connection URI  
- `DB_NAME` → MongoDB database name  
- `LOG_CHANNEL` → Channel ID for bot logs (bot must be admin there)  

---

<details>
<summary><b>🚀 Deploy to Heroku</b></summary>

[![Deploy](https://img.shields.io/badge/Deploy%20To%20Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/deploy?template=https://github.com/UHD-Botz/UHD-Auto-React-Bot)
</details>

<details>
<summary><b>🚀 Deploy to Koyeb</b></summary>

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=uhd-auto-react-bot&type=git&repository=UHD-Botz%2FUHD-Auto-React-Bot)
</details>

<details>
<summary><b>🚀 Deploy to Render</b></summary>

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/UHD-Botz/UHD-Auto-React-Bot)
</details>

<details>
<summary><b>🚀 Deploy to Railway</b></summary>

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/UHD-Botz/UHD-Auto-React-Bot)
</details>

<details>
<summary><b>💻 Deploy on VPS</b></summary>

```bash
# Clone The Repository
git clone https://github.com/UHD-Botz/UHD-Auto-React-Bot.git

# Enter Directory
cd UHD-Auto-React-Bot

# Install Required Packages
pip3 install -r requirements.txt

# Add Your API_ID, API_HASH, BOT_TOKEN, etc. in config.py

# Run The Bot
python3 bot.py
