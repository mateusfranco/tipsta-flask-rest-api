from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_redis import Redis

from config import app_config

db = SQLAlchemy()
redis = Redis()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    app.config['REDIS_HOST'] = 'redis'
    app.config['REDIS_PORT'] = 6379
    app.config['REDIS_DB'] = 0
    app.config['REDIS_PASSWORD'] = 'rootroot'

    redis.init_app(app)
    db.init_app(app)

    migrate = Migrate(app, db)

    from app import models

    return app