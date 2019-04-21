# project/server/__init__.py


import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_rest_jsonapi import Api
from project.server.routes import API_ROUTES
from flask_cors import CORS

# instantiate the extensions
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
marshmallow = Marshmallow()
api = Api()


def create_app(script_info=None):
    # instantiate the app
    app = Flask(
        __name__,
        template_folder="../client/templates",
        static_folder="../client/static",
    )

    # set config
    app_settings = os.getenv(
        "APP_SETTINGS", "project.server.config.DevelopmentConfig"
    )
    app.config.from_object(app_settings)

    # set up extensions
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)

    api = Api(app)
    CORS(app)
    # register blueprints
    from project.server.api.views import api_blueprint
    from project.server.user.views import user_blueprint

    app.register_blueprint(api_blueprint)
    app.register_blueprint(user_blueprint)

    for route_tuple in API_ROUTES:
        api.route(route_tuple[0], route_tuple[1], *route_tuple[2])
    # error handlers

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
