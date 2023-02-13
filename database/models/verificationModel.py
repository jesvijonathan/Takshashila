import datetime

from database.database import *

class Verification(db.Model):
    __tablename__ = 'verification'
    user_id = db.Column(db.String(50))
    email = db.Column(db.String(50), primary_key=True)  
    alt_hash = db.Column(db.String(300), primary_key=True)
    verification_for = db.Column(db.String(50), server_default="create_account") 
    status = db.Column(db.String(10), server_default="0") 
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    def __init__(self, data):
        self.user_id = data.get("user_id", None)
        self.email = data.get("email") 
        self.verification_for = data.get("verification_for", "create_account") 
        self.status = data.get("status", "0") 
        self.alt_hash = data.get("alt_hash", None) 
        self.created_at = datetime.datetime.now()

    def update(self, data):   
        if "alt_hash" in data:
            self.first_name = data.get("alt_hash", None)    

    def findExistingUser(email):
        return Verification.query.filter_by(email=email).first()
    
    def findExistingUserByHash(alt_hash):
        return Verification.query.filter_by(alt_hash=alt_hash).first()
