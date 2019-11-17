from .repositories import insert_user, find_user_by_id, find_user_by_email


async def register(name: str, email: str):
    data = {
        'name': name,
        'email': email,
    }
    return await insert_user(data)


async def detail_user(user_id: int):
    return await find_user_by_id(user_id)


async def detail_user_by_email(email: str):
    return await find_user_by_email(email)
