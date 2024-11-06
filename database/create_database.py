import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

Base = declarative_base()


class SQLDatabase:
    def __init__(self, database_connection_string):
        self.engine = create_async_engine(database_connection_string, pool_size=3, max_overflow=0)
        self.db = sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)

    async def create_database(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


