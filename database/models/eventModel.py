from database.database import db
import uuid


class Events(db.Model):
    __tablename__ = 'events'
    event_id = db.Column("id", db.String(50), primary_key=True)
    event_name = db.Column("event_name", db.String(100))
    batches = db.Column("batches", db.String(50))
    rules = db.Column("rules", db.String(5000))

    def __init__(self, data):
        self.event_id = str(uuid.uuid4())
        self.event_name = data["event_name"]
        self.batches = data["batches"]
        self.rules = data["rules"]

    def getAllEvents():
        return Events.query.all()

    def getSingleEvent(event_id):
        return Events.query.filter(Events.event_id == event_id).first().toJSON()
    
