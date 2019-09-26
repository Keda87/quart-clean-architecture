from .repositories import insert_todo


async def create_todo(name: str, user: dict):
    data = {
        'name': name,
        'user_id': user.get('id'),
    }
    return await insert_todo(data)

async def display_all_todo():
    pass


async def update_todo_status(todo_id: int):
    pass