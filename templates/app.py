from flask import Flask, redirect, url_for, render_template, request, Response, session, abort
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_required, UserMixin, login_user
from werkzeug.urls import url_parse
from flask_sqlalchemy import SQLAlchemy



login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




if __name__ == "__main__":
    app.run(debug=True)