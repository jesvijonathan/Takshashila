from flask import Blueprint , request
from database import db
from models import EventRegistration

# from controllers.userController import createUser

eventRoute = Blueprint("eventRoute", __name__, url_prefix='/api')

@eventRoute.route("/register", methods=['GET','POST'])
def eventregister():
    if (request.method == 'POST'):
        
        event = EventRegistration(request.json)
        db.session.add(event)
        db.session.commit()
        return 'ss'


