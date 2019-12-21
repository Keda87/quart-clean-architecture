import os
import jwt
from quart import Blueprint, request
from . import services as user_service
from ...helpers.decorators import auth_required

user_bp = Blueprint('user_bp', __name__)
SECRET = os.environ.get('SECRET_KEY')


@user_bp.route('/register', methods=['POST'])
async def register():
    payload = await request.json
    data = {
        'name': payload.get('name'),
        'email': payload.get('email'),
    }
    await user_service.register(**data)
    return {'data': data}, 201


@user_bp.route('/profile')
@auth_required()
async def profile():
    user_id = request.user.get('id')
    user = await user_service.detail_user(user_id)
    return {'data': dict(user)}


@user_bp.route('/auth', methods=['POST'])
async def auth():
    payload = await request.json

    user = await user_service.detail_user_by_email(payload['email'])
    user = dict(user)

    token = jwt.encode(user, SECRET, 'HS256')
    return {'data': {'token': token.decode('utf8')}}
