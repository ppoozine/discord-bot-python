import discord
from discord.ext import commands

from app.config import COMMAND_PREFIX, INTENTS
from app.database import engine
from app.models import Base


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        for intent, value in INTENTS.items():
            setattr(intents, intent, value)

        super().__init__(
            command_prefix=COMMAND_PREFIX,
            intents=intents
        )

    async def setup_hook(self):
        # 載入所有指令
        await self.load_extension("commands.user")

    async def on_ready(self):
        print(f'Bot is ready! Logged in as {self.user}')

        # 初始化資料庫
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("找不到該指令")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("你沒有權限執行此指令")
        else:
            await ctx.send(f"發生錯誤：{str(error)}")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def sync_commands(self, ctx):
        """同步斜線指令"""
        await self.tree.sync()
        await ctx.send("同步指令完成")


# 建立 bot 實例
bot = Bot()
