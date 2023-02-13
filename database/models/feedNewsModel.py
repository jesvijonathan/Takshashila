import datetime
import uuid
from database.database import db


class FeedNews(db.Model):
    __tablename__ = 'feed_news'
    id = db.Column('feed_news_id', db.String(50), primary_key=True)
    title = db.Column('title', db.String(50))
    description = db.Column('description', db.String(500))
    image = db.Column('image', db.String(500))
    link = db.Column('link', db.String(500))
    author = db.Column('author', db.String(50))
    created_at = db.Column('created_at', db.DateTime)
    updated_at = db.Column('updated_at', db.DateTime)

    def __init__(self, title, description, image, link, author):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.image = image
        self.link = link
        self.author = author
        self.created_at = datetime.datetime.utcnow
        self.updated_at = datetime.datetime.utcnow

    def getAllFeedNews():
        return FeedNews.query.all()
