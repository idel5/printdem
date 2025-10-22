from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from typing import AsyncGenerator, Any

engine = create_async_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

AsyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db() -> AsyncGenerator[Any, None]:
    async with AsyncSessionLocal() as session:
        yield session

async def init_db():
    from app.db.base_class import Base
    from app.models import product, order, design
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
