from flask import jsonify
from sqlalchemy import or_

from models import Users
from database import db


def createUser(data):
    if Users.query.filter(
        or_(
            user.username == data["namename"],
            user.email == data["email"],
        )
    ).first():
        return "A user with that username or email already exists."

    user = Users(data, data["password"])
    db.session.add(user)
    db.session.commit()

    return 'Ok'
