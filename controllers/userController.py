from flask import jsonify
from passlib.hash import pbkdf2_sha256

from models import Users
from database import db


def createUser(data):
    if (Users.findExistingUser(data["email"])):
        return {"message": "User with that email already exists."}, 409

    user = Users(data, pbkdf2_sha256.hash(data["password"]))
    db.session.add(user)
    db.session.commit()

    return 'Ok'
