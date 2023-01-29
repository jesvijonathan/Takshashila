from database import db
import datetime
import uuid


class EventRegistration(db.Model):
    __tablename__ = 'eventRegistration'
    event_registration_id = db.Column('id', db.String(50), primary_key=True)
    user_id = db.Column('user_id', db.String(50))
    event = db.Column('event', db.String(50))
    batch = db.Column('batch', db.String(50))
    created_at = db.Column('created_at', db.DateTime)
    updated_at = db.Column('updated_at', db.DateTime)

    def __init__(self, data):

        self.event_registration_id = str(uuid.uuid4())
        self.user_id = data["user_id"]
        self.event = data["event"]
        self.batch = data["batch"]
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def getAllRegistrations():
        return EventRegistration.query.all()
