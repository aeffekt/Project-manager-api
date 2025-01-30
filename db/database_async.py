# database.py
from typing import AsyncGenerator

from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from main import settings

DATABASE_URL = "sqlite+aiosqlite:///./test.db"  # Use a suitable database URL

engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        yield session
