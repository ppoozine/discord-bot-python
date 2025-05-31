# Discord Bot Python

這是一個使用 Python 和 Discord.py 開發的 Discord 機器人專案。該機器人提供了用戶資料查詢等功能，並使用 SQLAlchemy 進行資料庫操作。

## 專案結構

```
discord-bot-python/
├── app/
│   ├── __init__.py
│   ├── bot.py          # Bot 主程式
│   ├── config.py       # 設定檔
│   ├── database.py     # 資料庫連接設定
│   └── models.py       # 資料庫模型
├── commands/
│   ├── __init__.py
│   └── user.py         # 用戶相關命令
└── README.md
```

## 功能特點

- 使用 Discord.py 框架
- 支援斜線命令（Slash Commands）
- 使用 SQLAlchemy 進行資料庫操作
- 模組化的命令系統（Cogs）
- 完整的錯誤處理機制

## 安裝需求

- Python 3.12 或更高版本
- discord.py
- SQLAlchemy
- aiosqlite（sqlite 驅動）如使用其他資料庫（MySQL -> aiomysql、PostgreSQL -> asyncpg）

## 安裝步驟

1. clone 專案：
```bash
git clone [repository-url]
cd discord-bot-python
```

2. 安裝依賴套件：
```bash
pip install -r requirements.txt
```

3. 設定環境變數：
創建 `.env` 文件並設定以下變數：
```
DISCORD_TOKEN=your_discord_bot_token
DATABASE_URL=your_database_url
```

## 使用說明

### 啟動機器人

```bash
python -m app.bot
```

### 可用命令

- `/user <email>` - 查詢用戶資料
- `!sync_commands` - 同步斜線命令（需要管理員權限）

## 開發指南

### 添加新命令

1. 在 `commands` 目錄下創建新的命令文件（例如：`admin.py`）
2. 創建新的 Cog 類並定義命令
3. 在 `bot.py` 的 `setup_hook` 方法中添加新命令的載入

範例：
```python
# commands/admin.py
class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def new_command(self, ctx):
        await ctx.send("新命令！")

async def setup(bot):
    await bot.add_cog(AdminCommands(bot))
```

然後在 `bot.py` 中添加：
```python
async def setup_hook(self):
    await self.load_extension("commands.admin")
```

## 架構說明

### Bot 類（app/bot.py）
- 負責機器人的初始化和基本設定
- 處理命令載入和錯誤處理
- 管理資料庫初始化

### 命令系統（commands/）
- 使用 Cogs 組織命令
- 每個命令文件都是獨立的模組
- 通過 `setup` 函數註冊到 bot

### 資料庫（app/database.py, app/models.py）
- 使用 SQLAlchemy 進行資料庫操作
- 定義 DB Schema 和資料庫連接

## 注意事項

- 確保機器人有適當的 Discord 權限
- 定期備份資料庫
- 在正式環境中使用環境變數管理敏感資訊
