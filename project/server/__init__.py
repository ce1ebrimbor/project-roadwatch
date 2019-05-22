# project/server/__init__.py


import os

from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_rest_jsonapi import Api
from flask_cors import CORS

# instantiate the extensions
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
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
        "APP_SETTINGS", "project.server.config.ProductionConfig"
    )
    app.config.from_object(app_settings)

    # set up extensions
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)
    CORS(app)

    # register blueprints
    from project.server.user.views import user_blueprint

    app.register_blueprint(user_blueprint)

    # flask login
    from project.server.models import User

    login_manager.login_view = "user.login"
    # login_manager.login_message_category = "danger"
    from project.server.routes import API_ROUTES
    #API routes
    for route_tuple in API_ROUTES:
        api.route(route_tuple[0], route_tuple[1], *route_tuple[2])


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()


    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
