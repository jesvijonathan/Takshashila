from flask import request
from flask.views import MethodView

from flask_smorest import Blueprint

from controllers.userController import createUser
from database import Users

authBlp = Blueprint("AuthBlp", __name__, url_prefix='/api')


@authBlp.route("/signup")
class Signup(MethodView):
    def post(self):
        return createUser(request.get_json())


@authBlp.route("/users")
class Signup(MethodView):
    def get(self):
        return Users.getAllUsers()
