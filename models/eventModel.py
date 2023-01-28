from database import db


class EventRegistration(db.Model):
    __tablename__ = 'users'
    id = db.Column('id',db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer)
    event = db.Column('event', db.String(50))
    batch = db.Column('batcn', db.String(50))
    created_at = db.Column('created_at', db.DateTime)
    updated_at = db.Column('updated_at', db.DateTime)

    def __init__(self, user_id, event, batch, created_at, updated_at):
        self.user_id = user_id
        self.event = event
        self.batch = batch
        self.created_at = created_at
        self.updated_at = updated_at

    def getAllUsers():
        return EventRegistration.query.all();
