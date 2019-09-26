from .repositories import insert_todo, get_all_todo_by_user


async def create_todo(name: str, user: dict):
    data = {
        'name': name,
        'user_id': user.get('id'),
        'is_finished': False,
    }
    return await insert_todo(data)

async def get_all_todo(user):
    user_id = user.get('id')
    return await get_all_todo_by_user(user_id)


async def update_todo_status(todo_id: int):
    pass