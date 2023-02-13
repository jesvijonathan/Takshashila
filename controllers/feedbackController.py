from flask import jsonify
from database import db
from database import Feedback

def createFeedBack(data):
    feedBack = Feedback(data)
    db.session.add(feedBack)
    db.session.commit()
    return 'Ok'

def getFeedBack():
    return Feedback.getAllFeedback()
