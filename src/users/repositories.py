from ..config.database import DB_POOL


async def insert_user(data: dict):
    insert = """
    INSERT INTO users(name, email) 
    VALUES($1, $2)
    """
    name = data.get('name')
    email = data.get('email')

    pool = await DB_POOL
    async with pool.acquire() as conn:
        return await conn.execute(insert, name, email)