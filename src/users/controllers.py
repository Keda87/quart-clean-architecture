from quart import Blueprint, request
from . import services as user_service

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/register', methods=['POST'])
async def register():
    payload = await request.json
    data = {
        'name': payload.get('name'),
        'email': payload.get('email'),
    }
    await user_service.register(**data)
    return data


@user_bp.route('/profile')
async def profile():
    return 'profile'