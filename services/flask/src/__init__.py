from flask import Flask
from flask.logging import logging, default_handler
import os
import logging_loki
from .db import RedisDB
from openai import OpenAI

db = RedisDB()
# We need to pass the env OPENAI_API_KEY
openai_client = OpenAI()


def create_app():
    """
    Setup app
    """
    app = Flask(__name__)

    app.config["NAME"] = os.environ.get("NAME", "app")
    app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
    app.config["REDIS_URL"] = os.environ["REDIS_URL"]

    db.redis.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .chat import chat as chat_blueprint
    app.register_blueprint(chat_blueprint)

    from .bot import bot as bot_blueprint
    app.register_blueprint(bot_blueprint)

    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    return app


app = create_app()
