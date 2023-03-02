from database.database import db
import uuid


class Events(db.Model):
    __tablename__ = 'events'
    event_id = db.Column("id", db.String(50), primary_key=True)
    event_name = db.Column("event_name", db.String(100))

    event_incharge = db.Column("event_incharge", db.String(100))
    event_incharge_conatct = db.Column("event_incharge_conatct", db.String(100))
    event_fee = db.Column("event_fee", db.String(100))
    event_date = db.Column("event_date", db.String(100))
    event_venue = db.Column("event_venue", db.String(100))
    event_max_team = db.Column("event_max_team", db.String(100))
    event_prize = db.Column("event_prize", db.String(100))
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
    
