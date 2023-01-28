from database import db
import time

class EventRegistration(db.Model):
    __tablename__ = 'eventRegistration'
    id = db.Column('id',db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer)
    event = db.Column('event', db.String(50))
    batch = db.Column('batcn', db.String(50))
    created_at = db.Column('created_at', db.DateTime)
    updated_at = db.Column('updated_at', db.DateTime)

    def __init__(self, user_id, event, batch):
        self.user_id = user_id
        self.event = event
        self.batch = batch
        self.created_at = time.ctime()
        self.updated_at = time.ctime()

    def getAllUsers():
        return EventRegistration.query.all();
    
