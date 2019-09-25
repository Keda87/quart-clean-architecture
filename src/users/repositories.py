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


async def find_user_by_id(user_id: int):
    query = 'SELECT * FROM users WHERE id = $1'
    pool = await DB_POOL
    async with pool.acquire() as conn:
        return await conn.fetchrow(query, user_id)


async def find_user_by_email(email: str):
    query = 'SELECT * FROM users WHERE email = $1'
    pool = await DB_POOL
    async with pool.acquire() as conn:
        return await conn.fetchrow(query, email)