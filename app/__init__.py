from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS


db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    jwt.init_app(app)
    Migrate(app, db)
    from . import models
    from .resources import register_resources
    from .auth import register_user_resources

    api = Api(app)
    CORS(app)
    register_resources(api)
    register_user_resources(api)
    return app


