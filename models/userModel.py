from database import db

class Users(db.Model):  
    id = db.Column('user_id', db.Integer, primary_key = True)  
    email = db.Column('email',db.String(50))  
    phone_number= db.Column('phone_number',db.Integer)  
    first_name = db.Column('first_name',db.String(30))   
    last_name = db.Column('last_name',db.String(30))

    def __init__(self, name, email,phone_number,first_name,last_name):  
        self.name = name  
        self.email = email  
        self.phone_number = phone_number  
        self.first_name = first_name  
        self.last_name = last_name  

    def getAllUsers():
        return Users.query.all()
