# project/server/user/views.py


from flask import render_template, Blueprint, url_for, jsonify
from project.server import bcrypt, db
from project.server.models import Accident


api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/about")
def about():
    return jsonify(name="Project Roadwatch API",
                   version="0.1.0")
