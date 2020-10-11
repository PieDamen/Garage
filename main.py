from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main', __name__)

@main.route("/garage")
@login_required
def garage():
    return render_template("garage.html")


@main.route("/logs")
@login_required
def logs():
    return render_template("logs.html")
