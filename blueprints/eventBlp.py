from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request, jsonify

from database import db
from database import EventRegistration
from database import Events

# from controllers.userController import createUser

eventBlp = Blueprint("eventBlp", __name__, url_prefix='/api/events')


@eventBlp.route("/register")
class EventRegistration(MethodView):
    def post(self):
        event = EventRegistration(request.get_json())
        db.session.add(event)
        db.session.commit()
        return 'ss'


@eventBlp.route("/find/<event_id>")
class FindEvent(MethodView):
    def get(self, event_id):

        return jsonify(Events.getSingleEvent(event_id))

    def post(self):
        event = Events(request.get_json())
        db.session.add(event)
        db.session.commit()
        return 'ss'
