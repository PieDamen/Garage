from flask import Flask, redirect, url_for, render_template, request, Response, session, abort
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_required, UserMixin, login_user
from werkzeug.urls import url_parse

# config
app = Flask(__name__)
Bootstrap(app)
app.config.update(DEBUG=True, SECRET_KEY='2Png5xy8@')


@app.route("/login", methods=["GET", "POST"])
def login():
        return render_template('/login.html')


@app.route("/garage")
@login_required
def garage():
    return render_template("garage.html")


@app.route("/logs")
@login_required
def logs():
    return render_template("logs.html")


if __name__ == "__main__":
    app.run(debug=True)