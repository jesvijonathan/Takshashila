import datetime
import os

from database.database import db


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(500))
    phone_number = db.Column(db.Integer)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    institute = db.Column(db.String(30))
    degree = db.Column(db.String(50))
    branch = db.Column(db.String(50))
    graduate_year = db.Column(db.Integer)
    type = db.Column(db.String(50))
    type = db.Column(db.String(50),)
    qr_id = db.Column(db.String(50))
    user_qr = db.Column(db.String(50))
    google_id = db.Column(db.String(50))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, data, id, password):
        self.user_id = id
        self.name = data.get('name', '')
        self.email = data.get("email", '')
        self.password = password
        self.phone_number = data.get("phone_number", 0)
        self.first_name = data.get("first_name", '')
        self.last_name = data.get("last_name", '')
        self.institute = data.get("institute", '')
        self.degree = data.get("degree", '')
        self.branch = data.get("branch", '')
        self.graduate_year = data.get("graduate_year", 0)
        self.type = data.get("type", 'standard')
        self.qr_id = data.get("qr_id", '')
        self.user_qr = data.get(
            "user_qr", f"{os.getenv('SERVER_URL')}/static/users/{id}/{id}.png")
        self.google_id = data.get("google_id", '')
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def getAllUsers():
        return Users.query.all()

    def findExistingUser(email):
        return Users.query.filter_by(email=email).first()
