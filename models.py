from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
