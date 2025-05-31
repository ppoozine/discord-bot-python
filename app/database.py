from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .config import DATABASE_URL

# 建立非同步資料庫引擎
engine = create_async_engine(DATABASE_URL, echo=True)

# 建立非同步 session 工廠
async_session = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

# 取得資料庫連線
async def get_db():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close() 