from quart import Blueprint

todo_bp = Blueprint('todo_bp', __name__)

@todo_bp.route('/todos')
async def create_todo():
    return 'todo created'


@todo_bp.route('/todos/<int:id>')
async def update_todo():
    return 'todo created'


@todo_bp.route('/todos/<int:id>/archive')
async def archive_todo():
    return 'todo archived'