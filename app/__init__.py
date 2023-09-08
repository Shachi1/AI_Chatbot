
import logging.config

from app.utils.env import APPLICATION_ENV
# from celery import Celery
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from .config import config as app_config
from .core.views import core as core_blueprint
from .user.controller import userController
from .post.controller import postController
from .like.controller import likeController
from .comment.controller import commentController

# celery = Celery(__name__)
app = Flask(__name__)


URL_PREFIX = '/api/v1'


def create_app():
    # loading env vars from .env file
    load_dotenv()

    logging.config.dictConfig(app_config[APPLICATION_ENV].LOGGING)

    app = Flask(app_config[APPLICATION_ENV].APP_NAME)

    app.config.from_object(app_config[APPLICATION_ENV])

    CORS(app, resources={r'/api/*': {'origins': '*'}})

    # celery.config_from_object(app.config, force=True)
    # celery is not able to pick result_backend and hence using update
    # celery.conf.update(result_backend=app.config['RESULT_BACKEND'])

    app.register_blueprint(
        core_blueprint,
        url_prefix=URL_PREFIX
    )

    app.register_blueprint(
        userController,
        url_prefix=URL_PREFIX
    )

    app.register_blueprint(
        postController,
        url_prefix=URL_PREFIX
    )

    app.register_blueprint(
        likeController,
        url_prefix=URL_PREFIX
    )

    app.register_blueprint(
        commentController,
        url_prefix=URL_PREFIX
    )

    return app
