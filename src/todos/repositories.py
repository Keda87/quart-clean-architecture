from quart import current_app


async def insert_todo(data: dict):
    sql = 'INSERT INTO todos(name, user_id) VALUES($1, $2)'

    name = data.get('name')
    user_id = data.get('user_id')
    async with current_app.db_pool.acquire() as conn:
        return await conn.execute(sql, name, user_id)


async def get_all_todo():
    pass


async def update_todo(data, todo_id):
    pass