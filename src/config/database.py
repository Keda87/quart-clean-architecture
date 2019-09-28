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

   def __init__(self):
      if ConnectionPool._POOL != None:
         raise Exception("This class is a singleton!")
      else:
         ConnectionPool._POOL = self

   @classmethod
   async def get_pool(cls):
      if cls._POOL == None:
         cls._POOL = await asyncpg.create_pool(DB_DSN, command_timeout=60)
      return cls._POOL
