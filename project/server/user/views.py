# project/server/user/views.py

from flask import Blueprint, render_template, request, flash
from project.server.models import User
from project.server import db

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/")
def home():
    return render_template("login.html", signup=True)


@user_blueprint.route("/signup", methods=["POST"])
def auth():
    email = request.form.get('email')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmPassword')

    user = User.query.filter_by(email=email).first()

    if user is None:
        user = User(email=email)
        user.set_password(password=password)
        db.session.add(user)
        db.session.commit()
        flash('Your registration was successfull, you can sign in now.')
        return render_template("login.html", sigup=False)
    else:
        return 'User already exists'


@user_blueprint.route("/docs")
def docs():
    return render_template("docpage.html")
