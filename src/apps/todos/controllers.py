from quart import Blueprint, request

from . import services as todo_service
from ...helpers.decorators import auth_required

todo_bp = Blueprint("todo_bp", __name__)


@todo_bp.route("/todos", methods=["POST"])
@auth_required()
async def create_todo():
    user = request.user

    payload = await request.json
    name = payload.get("name")
    await todo_service.create_todo(name, user)

    return {"data": {"name": name, "user": user}}, 201


@todo_bp.route("/todos", methods=["GET"])
@auth_required()
async def list_todo():
    data = await todo_service.get_all_todo(request.user)
    data = list(data)

    return {"data": [dict(i) for i in data]}


@todo_bp.route("/todos/<int:id>", methods=["PATCH"])
@auth_required()
async def update_todo(id):
    payload = await request.json
    is_finished = payload.get("is_finished")
    data = await todo_service.update_todo_status(id, is_finished)
    data = dict(data)

    return {"data": data}
