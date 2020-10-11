from flask import Flask, redirect, url_for, render_template, request, Response, session, abort
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_required, UserMixin, login_user
from werkzeug.urls import url_parse
from flask_sqlalchemy import SQLAlchemy

# config
app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)



@app.route("/login", methods=["GET", "POST"])
def login():
        return render_template('/login.html')


@app.route("/garage")
def garage():
    return render_template("garage.html")


@app.route("/logs")
def logs():
    return render_template("logs.html")


if __name__ == "__main__":
    app.run(debug=True)