from flask import Blueprint, render_template, url_for, redirect, request
from .models import User
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)


@auth.route("/login")
def login():
    return render_template('/login.html')


@auth.route("/login", methods=["POST"])
def login_post():
    user = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(user=user).first()

    if not user and not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.garage'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))