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


@todo_bp.route('/todos', methods=['GET'])
async def list_todo():
    headers = request.headers.to_dict()
    token = headers.get('Authorization')
    try:
        user = jwt.decode(token, SECRET, 'HS256')
    except Exception:
        return {'error': 'Authorization is required'}, 401

    data = await todo_service.get_all_todo(user)
    data = list(data)

    return {'data': [dict(i) for i in data]}


@todo_bp.route('/todos/<int:id>', methods=['PATCH'])
async def update_todo(id):
    headers = request.headers.to_dict()
    token = headers.get('Authorization')
    try:
        user = jwt.decode(token, SECRET, 'HS256')
    except Exception:
        return {'error': 'Authorization is required'}, 401

    payload = await request.json
    is_finished = payload.get('is_finished')
    data = await todo_service.update_todo_status(id, is_finished)
    data = dict(data)

    return {'data': data}
