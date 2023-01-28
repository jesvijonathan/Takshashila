import datetime
import uuid
from sqlalchemy import or_

from database import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('user_id', db.String(50), primary_key=True)
    email = db.Column('email', db.String(50))
    password = db.Column('password', db.String(100))
    phone_number = db.Column('phone_number', db.Integer)
    first_name = db.Column('first_name', db.String(30))
    last_name = db.Column('last_name', db.String(30))
    institute = db.Column('institute', db.String(30))
    degree = db.Column('degree', db.String(50))
    branch = db.Column('branch', db.String(50))
    graduate_year = db.Column('graduate_year', db.Integer)
    type = db.Column('type', db.String(50))
    qr_id = db.Column('qr_id', db.String(50))
    google_id = db.Column('google_id', db.String(50))
    created_at = db.Column('created_at', db.DateTime)
    updated_at = db.Column('updated_at', db.DateTime)

    def __init__(self, data, password):
        self.id = str(uuid.uuid4())
        self.name = data["name"]
        self.email = data["email"]
        self.password = password
        self.phone_number = data["phone_number"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.institute = data["institute"]
        self.degree = data["degree"]
        self.branch = data["branch"]
        self.graduate_year = data["graduate_year"]
        self.type = data["type"]
        self.qr_id = data["qr_id"]
        self.google_id = data["google_id"]
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def getAllUsers():
        return Users.query.all()

    def findExistingUser(email):
        return Users.query.filter(
            or_(
                Users.email == email,
            )
        ).first()
