import time
from database import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('user_id', db.String(50), primary_key=True)
    email = db.Column('email', db.String(50))
    password = db.Column('password', db.String(50))
    phone_number = db.Column('phone_number', db.Integer)
    first_name = db.Column('first_name', db.String(30))
    last_name = db.Column('last_name', db.String(30))
    institute = db.Column('institute', db.String(30))
    degree = db.Column('degree', db.String(50))
    branch = db.Column('branch', db.String(50))
    graduate_year = db.Column('graduate_year', db.Integer)
    type = db.Column('type', db.String(50))
    date_join = db.Column('date_join', db.Date)
    qr_id = db.Column('qr_id', db.String(50))
    qr_date = db.Column('qr_date', db.String(50))
    google_id = db.Column('google_id', db.String(50))
    created_at = db.Column('created_at', db.DateTime)
    updated_at = db.Column('updated_at', db.DateTime)

    def __init__(self, name, email, phone_number, first_name, last_name, institute, degree, branch, graduate_year, type, date_join, qr_id, qr_date, google_id):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.institute = institute
        self.degree = degree
        self.branch = branch
        self.graduate_year = graduate_year
        self.type = type
        self.date_join = date_join
        self.qr_id = qr_id
        self.qr_date = qr_date
        self.google_id = google_id
        self.created_at = time.ctime()
        self.updated_at = time.ctime()

    def getAllUsers():
        return Users.query.all();
