from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/garage")
def garage():
    return render_template("garage.html")


@main.route("/logs")
def logs():
    return render_template("logs.html")
