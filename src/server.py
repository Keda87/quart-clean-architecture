from quart import Quart

from .config.database import ConnectionPool
from .apps.todos.controllers import todo_bp
from .apps.users.controllers import user_bp


app = Quart(__name__)
app.register_blueprint(todo_bp)
app.register_blueprint(user_bp)


@app.before_serving
async def on_start():
    app.db_pool = await ConnectionPool.get_pool()


@app.after_serving
async def on_stop():
    await app.db_pool.close()


@app.route("/")
async def index():
    return {
        "status": "ok",
    }
