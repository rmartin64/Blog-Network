from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from configuration import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import RotatingFileHandler
import os

blog = Flask(__name__)
blog.config.from_object(Config)
db = SQLAlchemy(blog)
migrate = Migrate(blog, db)
login = LoginManager(blog)
login.login_view = 'login'
bootstrap = Bootstrap(blog)
moment = Moment(blog)

if not blog.debug:

    if blog.config['LOG_TO_STDOUT']:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        blog.logger.addHandler(stream_handler)
    else:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/blog.log', maxBytes=10240,
                                        backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        blog.logger.addHandler(file_handler)

    blog.logger.setLevel(logging.INFO)
    blog.logger.info('Blog Network startup')

from main import urls, models, errors
