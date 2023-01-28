import time
from database import db


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column('feedback_id', db.String(50), primary_key=True)
    feedback = db.Column('feedback', db.String(200))
    description = db.Column('description', db.String(500))
    image = db.Column('image', db.String(500))
    link = db.Column('link', db.String(500))
    author = db.Column('author', db.String(50))
    created_at = db.Column('created_at', db.DateTime)
    updated_at = db.Column('updated_at', db.DateTime)

    def __init__(self, id, title, description, image, link, author):
        self.id = id
        self.title = title
        self.description = description
        self.image = image
        self.link = link
        self.author = author
        self.created_at = time.ctime()
        self.updated_at = time.ctime()

    def getAllFeedback():
        return Feedback.query.all()
