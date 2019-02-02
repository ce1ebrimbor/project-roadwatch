# project/server/user/views.py


from flask import Blueprint, jsonify
from project.server.models import Accident
from project.server import db

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/about")
def about():
    return jsonify(name="Project Roadwatch API",
                   version="0.1.0")

@api_blueprint.route("/accidents")
def accidents():
    all_accidents = Accident.query.all()
    return str(all_accidents)
