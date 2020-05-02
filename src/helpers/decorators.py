import os
import jwt
from functools import wraps
from quart import request

SECRET = os.environ.get("SECRET_KEY")


def auth_required():
    def wrapper(func):
        @wraps(func)
        async def check_token(*args, **kwargs):
            headers = request.headers.to_dict()
            token = headers.get("Authorization")
            try:
                user = jwt.decode(token, SECRET, "HS256")
                request.user = user
            except Exception:
                return {"error": "Authorization is required"}, 401

        return check_token

    return wrapper
