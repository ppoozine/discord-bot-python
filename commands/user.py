from discord.ext import commands
from sqlalchemy import select

from app.database import get_db
from app.models import User


class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def user(self, ctx, email: str):
        """查詢用戶資料"""
        async for session in get_db():
            try:
                stmt = select(User).where(User.email == email)
                result = await session.execute(stmt)
                user = result.scalar_one_or_none()

                if user:
                    await ctx.send(
                        f"找到用戶：\n"
                        f"Email: {user.email}\n"
                        f"Username: {user.username}\n"
                        f"創建時間: {user.created_at}"
                    )
                else:
                    await ctx.send(f"找不到使用 email {email} 的用戶")
            except Exception as e:
                await ctx.send(f"查詢時發生錯誤：{str(e)}")


async def setup(bot):
    await bot.add_cog(UserCommands(bot))
