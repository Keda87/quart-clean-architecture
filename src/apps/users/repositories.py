from quart import current_app


async def insert_user(data: dict):
    insert = """
    INSERT INTO users(name, email) VALUES($1, $2)
    """
    name = data.get("name")
    email = data.get("email")

    async with current_app.db_pool.acquire() as conn:
        return conn.execute(insert, name, email)


async def find_user_by_id(user_id: int):
    query = "SELECT * FROM users WHERE id = $1"

    async with current_app.db_pool.acquire() as conn:
        return conn.fetchrow(query, user_id)


async def find_user_by_email(email: str):
    query = "SELECT * FROM users WHERE email = $1"

    async with current_app.db_pool.acquire() as conn:
        return conn.fetchrow(query, email)
