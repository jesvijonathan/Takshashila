from flask import Blueprint

from models import EventRegistration

# from controllers.userController import createUser

eventRoute = Blueprint("eventRoute", __name__, url_prefix='/api')

@eventRoute.route("/register", methods=['GET','POST'])
def do_get():
    return EventRegistration.getAllUsers()