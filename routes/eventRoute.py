from flask import Blueprint , request

from models import EventRegistration

# from controllers.userController import createUser

eventRoute = Blueprint("eventRoute", __name__, url_prefix='/api')

@eventRoute.route("/register", methods=['GET','POST'])
def eventregister():
    if (request.method == 'POST'):
        
        data = EventRegistration(request.json["user_id"],request.json["event"],request.json["batch"])

        return data


