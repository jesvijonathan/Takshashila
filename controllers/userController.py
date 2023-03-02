from flask import jsonify, redirect
from passlib.hash import pbkdf2_sha256
import qrcode
import uuid
import os

from database import Users, db

from controllers.verificationController import create_verification

server_path = "/home/takshashila/Takshashila-2023-Backend/"

def generate_qr(data):
    #data = id
    userQr = qrcode.make(data)    
    userQr.save(server_path + "users/" + data+  ".png")


def createUser(data, verification=0):
    if (Users.findExistingUser(data["email"])):
        
        return 0

    id = str(uuid.uuid4())
    hashed_pass = pbkdf2_sha256.hash(data["password"]) 
    data['password'] = hashed_pass
    data['verified'] = verification

    generate_qr(id)

    user = Users(data, id, hashed_pass)
    db.session.add(user)
    db.session.commit()


    
    user_db_data = Users.findExistingUser(data["email"])  
    return user_db_data


def createUser_oauth(data):
    if user_in_db := (Users.findExistingUser(data["email"])): 
        return user_in_db

    id = str(uuid.uuid4())  

    
    data['verified'] = 1
    
    generate_qr(id)

    user = Users(data, id)

    db.session.add(user)
    db.session.commit() 

    user_db_data = Users.findExistingUser(data["email"])
    
    return user_db_data

def update_user_details(data):
    user = Users.query.filter_by(hash=data['hash']).first() 

    if not user:
        return -1 
    
    # user = Users.update_data(data) 
    li = [  'phone_number',
            'first_name'
            'last_name',
            'institute',
            'degree',
            'branch',
            'graduate_year',
            'hash',
            'stage_two']
     
    user.update(data)
    db.session.add(user)
    db.session.commit()  

def update_user_details_veri(data):
    user = Users.query.filter_by(email=data['email']).first() 

    if not user:
        return -1  
     
    user.update(data)
    db.session.add(user)
    db.session.commit()  
    
    user_db_data = Users.findExistingUser(data["email"])
    
    return user_db_data
 
    # user.phone_number = data.get("phone_number", None)
    # user.first_name = data.get("first_name", None)
    # user.last_name = data.get("last_name", None)
    # user.stage_two = data.get("stage_two", '0')
    # user.institute = data.get("institute", None)
    # user.degree = data.get("degree", None)
    # user.branch = data.get("branch", None)
    # user.graduate_year = data.get("graduate_year", None) 
