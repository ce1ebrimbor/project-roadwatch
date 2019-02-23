# project/server/__init__.py


import os

from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_rest_jsonapi import Api
from project.server.resources import AccidentList, LieuList, UsagerList
from project.server.resources import VehiculeList, UsagerRelationship
from project.server.resources import LieuDetail, AccidentDetail, UsagerDetail
from project.server.resources import VehiculeDetail, AccidentRelationship
from project.server.resources import LieuRelationship, VehiculeRelationship

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

    app.register_blueprint(api_blueprint)

    api.route(AccidentList, 'accident_list', '/accident')
    api.route(AccidentDetail, 'accident_detail', '/accident/<int:id>',
                                                 '/usager/<int:uid>/accident',
                                                 '/lieu/<int:lid>/accident',
                                                 '/vehicule/<int:vid>/accident')

    api.route(AccidentRelationship, 'accident_usagers',
                                    '/accident/<int:id>/relationships/usager')
    api.route(AccidentRelationship, 'accident_lieu',
                                    '/accident/<int:id>/relationships/lieu')
    api.route(AccidentRelationship, 'accident_vehicule',
                                    '/accident/<int:id>/relationships/vehicule')

    api.route(LieuList, 'lieu_list', '/lieu')

    api.route(LieuDetail, 'lieu_detail', '/lieu/<int:id>',
                                         '/accident/<int:aid>/lieu')

    api.route(LieuRelationship, 'lieu_accident',
                                '/lieu/<int:id>/relationships/accident')

    api.route(UsagerList, 'usager_list', '/usager',
                                         '/accident/<int:id>/usager')

    api.route(UsagerDetail, 'usager_detail', '/usager/<int:id>')

    api.route(UsagerRelationship, 'usager_accident',
                                  '/usager/<int:id>/relationships/accident')

    api.route(VehiculeList, 'vehicule_list', '/vehicule',
                                             '/accident/<int:id>/vehicule')

    api.route(VehiculeDetail, 'vehicule_detail', '/vehicule/<int:id>')

    api.route(VehiculeRelationship, 'vehicule_accident',
                                    '/vehicule/<int:id>/relationships/accident')
    # error handlers

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
