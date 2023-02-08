import datetime
import os

import hashlib
import uuid

from database.database import db


def generate_hash():
    encrpass = str(uuid.uuid4())
    encrpass = hashlib.sha256(encrpass.encode())
    Hash = encrpass.hexdigest()
    return Hash

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(500), server_default=None)
    phone_number = db.Column(db.Integer, server_default=None)
    first_name = db.Column(db.String(30), server_default='')
    last_name = db.Column(db.String(30), server_default='')
    stage_two = db.Column(db.Integer, server_default='0')
    institute = db.Column(db.String(30), server_default=None)
    degree = db.Column(db.String(50), server_default=None)
    branch = db.Column(db.String(50), server_default=None)
    graduate_year = db.Column(db.Integer, server_default=None)
    type = db.Column(db.String(50), server_default="student") 
    
    qr_id = db.Column(db.String(50), server_default=None)
    user_qr = db.Column(db.String(300), server_default=None)

    hash = db.Column(db.String(300), primary_key=True)
    google_id = db.Column(db.String(50), server_default=None)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    def __init__(self, data, id, password=None):
        self.user_id = id
        self.name = data.get('name', None)
        self.email = data.get("email")
        self.password = password
        self.phone_number = data.get("phone_number", None)
        self.first_name = data.get("first_name", None)
        self.last_name = data.get("last_name", None)
        self.stage_two = data.get("stage_two", '0')
        self.institute = data.get("institute", None)
        self.degree = data.get("degree", None)
        self.branch = data.get("branch", None)
        self.graduate_year = data.get("graduate_year", None)
        self.type = data.get("type", 'standard') 
        self.qr_id = data.get("qr_id", None)
        self.user_qr = data.get(
            "user_qr", f"{os.getenv('SERVER_URL')}/static/users/{id}/{id}.png")
        self.hash = generate_hash()
        self.google_id = data.get("google_id", None)
        self.created_at = datetime.datetime.now()

    def update(self, data):   
        self.phone_number = data.get("phone_number", None)
        self.first_name = data.get("first_name", None)
        self.last_name = data.get("last_name", None)
        self.stage_two = data.get("stage_two", '0')
        self.institute = data.get("institute", None)
        self.degree = data.get("degree", None)
        self.branch = data.get("branch", None)
        self.graduate_year = data.get("graduate_year", None)  

    def getAllUsers():
        return Users.query.all()

    def findExistingUser(email):
        return Users.query.filter_by(email=email).first()
    
    def findExistingUserByHash(hash):
        return Users.query.filter_by(hash=hash).first()
