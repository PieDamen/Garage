from flask import render_template
from app import app

@app.route("/login", methods=["GET", "POST"])
def login():
        return render_template('/login.html')


@app.route("/garage")
def garage():
    return render_template("garage.html")


@app.route("/logs")
def logs():
    return render_template("logs.html")