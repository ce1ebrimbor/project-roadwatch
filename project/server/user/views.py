# project/server/user/views.py

import flask_login
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import current_app, jsonify
from project.server.models import User
from project.server import db
from project.server import login_manager
from flask_login import current_user
from validate_email import validate_email
import jwt
import datetime

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("user.docs"))
    else:
        return render_template("login.html", signup=False)


@user_blueprint.route("/signup", methods=["POST"])
def auth():
    email = request.form.get('email')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmPassword')

    user = User.query.filter_by(email=email).first()

    if user is None:
        is_valid = validate_email(email)

        if not is_valid:
            flash('Invalid email', 'danger')
            return render_template("login.html", signup=True)

        user = User(email=email)

        if password == confirmPassword:
            user.set_password(password=password)
            db.session.add(user)
            db.session.commit()
            flash('Your registration was successfull, you can sign in now.', 'success')
            return render_template("login.html", signup=False)
        else:
            flash('Passwords do not match.', 'warning')
            return render_template("login.html", signup=True)
    else:
        flash('User already exists', 'warning')
        return render_template('login.html', signup=True)



@user_blueprint.route("/signin", methods=["POST"])
def signin():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()

    if user is None:
        flash("Wrong username or password", "danger")
    else:
        if user.check_password(password):
            flask_login.login_user(user)
        else:
            flash("Wrong username or password", "danger")
    return redirect(url_for("user.home"))



@user_blueprint.route("/signout")
@flask_login.login_required
def signout():
    flask_login.logout_user()
    flash('Disconnected successfully.', 'success')
    return redirect(url_for("user.home"))


@user_blueprint.route("/docs")
def docs():
    return render_template("docpage.html")


@user_blueprint.route("/aboutpage")
def about():
    return render_template("about.html")


@user_blueprint.route("/dashboard")
@flask_login.login_required
def dashboard():
    return render_template("dashboard.html", generated_token=None)


@user_blueprint.route("/dashboardtk")
@flask_login.login_required
def dashboardtk():
    id = current_user.get_id()
    username = current_user.email

    token = jwt.encode({'id': id,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=365)},
                        current_app.config['SECRET_KEY'])
    return render_template("dashboard.html", generated_token=token.decode("utf-8"))
