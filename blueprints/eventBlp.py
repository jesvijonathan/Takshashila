from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request

from database import db
from models import EventRegistration

# from controllers.userController import createUser

eventBlp = Blueprint("eventBlp", __name__, url_prefix='/api/event')


@eventBlp.route("/register")
class Event(MethodView):
    def post():
        event = EventRegistration(request.json)
        db.session.add(event)
        db.session.commit()
        return 'ss'
