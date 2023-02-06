from flask import jsonify

from models import Feedback
from database import db


def createFeedBack(data):
    feedBack = Feedback(data)
    db.session.add(feedBack)
    db.session.commit()
    return 'Ok'


def getFeedBack():
    return Feedback.getAllFeedback()
