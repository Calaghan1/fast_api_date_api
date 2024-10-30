from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from database.models import Participant

DATABASE_URL = "sqlite+aiosqlite:///./test.db"  # Используем SQLite для простоты
engine = create_async_engine(DATABASE_URL, echo=False)
async_session = sessionmaker(
    bind=engine, 
    class_=AsyncSession,
    expire_on_commit=False
)

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Participant.metadata.create_all)
        
