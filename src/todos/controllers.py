import os
import jwt
from quart import Blueprint, request
from . import services as todo_service

todo_bp = Blueprint('todo_bp', __name__)
SECRET = os.environ.get('SECRET_KEY')


@todo_bp.route('/todos', methods=['POST'])
async def create_todo():
    headers = request.headers.to_dict()
    token = headers.get('Authorization')
    try:
        user = jwt.decode(token, SECRET, 'HS256')
    except Exception:
        return {'error': 'Authorization is required'}, 401

    payload = await request.json
    name = payload.get('name')
    await todo_service.create_todo(name, user)
    return {'data': {'name': name, 'user': user}}, 201


@todo_bp.route('/todos/<int:id>')
async def update_todo():
    return 'todo created'


@todo_bp.route('/todos/<int:id>/archive')
async def archive_todo():
    return 'todo archived'