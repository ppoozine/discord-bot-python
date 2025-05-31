import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# Discord Bot 設定
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
COMMAND_PREFIX = "!"

# 資料庫設定
DATABASE_URL = "sqlite+aiosqlite:///users.db"

# Bot 權限設定
INTENTS = {
    "message_content": True,
    "members": True,
    "guilds": True
} 