# project/server/__init__.py


import os

from flask import Flask, render_template
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_rest_jsonapi import Api
from project.server.models import AccidentList

# instantiate the extensions
login_manager = LoginManager()
bcrypt = Bcrypt()
toolbar = DebugToolbarExtension()
bootstrap = Bootstrap()
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
    bcrypt.init_app(app)
    toolbar.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    marshmallow.init_app(app)
    api = Api(app)

    # register blueprints
    from project.server.api.views import api_blueprint

    api.route(AccidentList, 'accident_list', '/accidents')
    # error handlers

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
