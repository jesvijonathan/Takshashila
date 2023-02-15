import datetime
import os


from database.database import db
from utils.email_system import generate_hash


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(50), primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(500), server_default=None)
    phone_number = db.Column(db.VARCHAR(16), server_default=None)
    verified = db.Column(db.VARCHAR(16), server_default='0')
    first_name = db.Column(db.String(30), server_default='')
    last_name = db.Column(db.String(30), server_default='')
    stage_two = db.Column(db.Integer, server_default='0')
    institute = db.Column(db.String(128), server_default=None)
    degree = db.Column(db.String(128), server_default=None)
    branch = db.Column(db.String(128), server_default=None)
    graduate_year = db.Column(db.String(50), server_default=None)
    type = db.Column(db.String(50), server_default="student") 
    
    qr_id = db.Column(db.String(50), server_default=None)
    user_qr = db.Column(db.String(300), server_default=None)

    hash = db.Column(db.String(300), primary_key=True)
    google_id = db.Column(db.String(100), server_default=None)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    def __init__(self, data, id, password=None):
        self.user_id = id
        self.name = data.get('name', None)
        self.email = data.get("email")
        self.password = password
        self.phone_number = data.get("phone_number", None)
        self.verified = data.get("verified", '0') 
        self.first_name = data.get("first_name", None)
        self.last_name = data.get("last_name", None)
        self.stage_two = data.get("stage_two", '0')
        self.institute = data.get("institute", None)
        self.degree = data.get("degree", None)
        self.branch = data.get("branch", None)
        self.graduate_year = data.get("graduate_year", None)
        self.type = data.get("type", 'student') 
        self.qr_id = data.get("qr_id", None)
        self.user_qr = data.get(
            "user_qr", f"{os.getenv('SERVER_URL')}/static/users/{id}/{id}.png")
        self.hash = generate_hash()
        self.google_id = data.get("google_id", None)
        self.created_at = datetime.datetime.now()

    def update(self, data):   
        
        if "name" in data:
            self.name = data.get("name", None)
        if "phone_number" in data:
            self.phone_number = data.get("phone_number", None)
        if "first_name" in data:
            self.first_name = data.get("first_name", None) 
        if "last_name" in data:
            self.last_name = data.get("last_name", None) 
        if "verified" in data: 
            self.verified = data.get("verified", '0') 
        if "stage_two" in data:
            self.stage_two = data.get("stage_two", '0') 
        if "institute" in data:
            self.institute = data.get("institute", None)    
        if "degree" in data:
            self.degree = data.get("degree", None) 
        if "branch" in data:
            self.branch = data.get("branch", None) 
        if "graduate_year" in data:
            self.graduate_year = data.get("graduate_year", None)     
        if "stage_two" in data:
            self.stage_two = data.get("stage_two", None)    
        if "hash" in data:
            self.hash = data.get("hash", None)  
    def getAllUsers():
        return Users.query.all()

    def findExistingUser(email):
        return Users.query.filter_by(email=email).first()
    
    def findExistingUserByHash(hash):
        return Users.query.filter_by(hash=hash).first()
