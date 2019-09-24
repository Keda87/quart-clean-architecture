import asyncpg
import os


DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_PASS = os.environ.get('DB_PASS')
DB_USER = os.environ.get('DB_USER')
DB_DSN = f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


class ConnectionPool:
    _POOL = None

    class Pool:
        @staticmethod
        async def get_instance():
            return await asyncpg.create_pool(DB_DSN, command_timeout=60)
    
    @classmethod
    async def get_pool(cls):
        if cls._POOL is not None:
            return await cls._POOL
        return await cls.Pool.get_instance()


DB_POOL = ConnectionPool.get_pool()