from quart import current_app


async def insert_todo(data: dict):
    sql = """
    INSERT INTO 
        todos(name, user_id, is_finished) 
    VALUES($1, $2, $3)
    """

    name = data.get('name')
    user_id = data.get('user_id')
    is_finished = data.get('is_finished')
    async with current_app.db_pool.acquire() as conn:
        return await conn.execute(sql, name, user_id, is_finished)


async def get_all_todo_by_user(user_id):
    sql = """
    SELECT 
        td.id,
        td.name,
        td.is_finished
    FROM
        users AS us 
    INNER JOIN
        todos AS td
    ON us.id = td.user_id 
    WHERE us.id = $1
    """
    async with current_app.db_pool.acquire() as conn:
        return await conn.fetch(sql, user_id)


async def get_todo_by_id(todo_id):
    sql = 'SELECT * FROM todos WHERE id = $1'

    async with current_app.db_pool.acquire() as conn:
        return await conn.fetchrow(sql, todo_id)


async def update_todo(data: dict, todo_id: int):
    set_values = [
        f'SET {key} = {"true" if value else "false"}'
        for key, value in data.items()
    ]
    set_values = ', '.join(set_values)

    sql = f'UPDATE todos {set_values} WHERE id = $1'
    async with current_app.db_pool.acquire() as conn:
        return await conn.execute(sql, todo_id)