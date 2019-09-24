from quart import Quart

from .todos.controllers import todo_bp
from .users.controllers import user_bp


app = Quart(__name__)
app.register_blueprint(todo_bp)
app.register_blueprint(user_bp)


@app.route('/')
async def index():
    return {
        'status': 'ok',
    }