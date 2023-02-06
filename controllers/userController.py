from flask import jsonify
from passlib.hash import pbkdf2_sha256
import qrcode
import uuid
import os

from database import Users, db


def createUser(data):
    # if (Users.findExistingUser(data["email"])):
    #     return {"message": "User with that email already exists."}, 409

    id = str(uuid.uuid4())  
    hashed_pass = pbkdf2_sha256.hash(data["password"])
    data.update({'password': hashed_pass})
    userQr = qrcode.make(data)
    os.mkdir(f"./static/users/{id}")
    userQr.save(f"./static/users/{id}/{id}.png")

    user = Users(data, id, hashed_pass)
    db.session.add(user)
    db.session.commit()
    print(Users.findExistingUser(data['email']))
    return "Users.findExistingUser(data['email'])"
