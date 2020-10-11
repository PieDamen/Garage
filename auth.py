from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route("/login")
def login():
    return render_template('/login.html')


@auth.route("/login", methods=["POST"])
def login_post():

        user = User.query.filter_by(user=request.form('username')).first()
        if not user and not request.form('password'):
            return '<h1>Invalid credentials, please try again</h1>'

        login_user(user)
        return redirect(url_for('Garage'))

