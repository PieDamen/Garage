from flask import Blueprint, render_template, Response
from flask_login import login_required
from . import gen
import subprocess

main = Blueprint('main', __name__)

@main.route("/garage")
@login_required
def garage():
    return render_template("garage.html")


@main.route("/logs")
@login_required
def logs():
    return render_template("logs.html")


@main.route('/video_feed')
@login_required
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@main.route('/exec')
@login_required
def exec():
    subprocess.Popen(['python', '/home/pi/Desktop/GarageDeur/Scripts/RelaySwitch.py'])
    return render_template('garage.html')