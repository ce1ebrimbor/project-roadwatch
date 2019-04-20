# project/server/user/views.py

from flask import Blueprint, render_template

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/")
def home():
    return render_template("login.html")
