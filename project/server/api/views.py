# project/server/user/views.py


from flask import Blueprint, jsonify

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/about")
def about():
    return jsonify(name="Project Roadwatch API",
                   version="0.1.0")
