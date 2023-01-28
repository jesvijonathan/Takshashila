from database import db


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column('feedback_id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(50))
    description = db.Column('description', db.String(500))
    image = db.Column('image', db.String(500))
    link = db.Column('link', db.String(500))
    author = db.Column('author', db.String(50))

    def __init__(self, id, title, description, image, link, author):
        self.id = id
        self.title = title
        self.description = description
        self.image = image
        self.link = link
        self.author = author

    def getAllFeedback():
        return Feedback.query.all()
