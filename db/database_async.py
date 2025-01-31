"""
This file initializes the asynchronous SQLModel database and provides a dependency
function to get an asynchronous database session. It uses settings from the
'main' module to configure the database connection.
"""
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from main import settings

DATABASE_URL = settings.db_async_url

async_engine = create_async_engine(DATABASE_URL, 
                            echo=True,
                            future=True,                            
                            )


async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_async_session() -> AsyncSession:
   async_session = sessionmaker(
       bind=async_engine, class_=AsyncSession, expire_on_commit=False
   )
   async with async_session() as session:
       yield session
