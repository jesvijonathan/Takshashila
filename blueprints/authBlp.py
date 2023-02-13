from flask import request, jsonify
from flask.views import MethodView

from flask_smorest import Blueprint

from controllers.userController import createUser
from database import Users

import json

authBlp = Blueprint("AuthBlp", __name__, url_prefix='/api')


@authBlp.route("/signup")
class Signup(MethodView):
    def post(self):
        return createUser(request.get_json())


@authBlp.route("/users")
class Signup(MethodView):
    def get(self):
        all_users = Users.getAllUsers()
        tmp = []
        tmp1= []
        
        for p in all_users:
            tmp = []
            for i in all_users:
                tmp.append(i.__dict__.items())
                # print(i.__dict__.items())
            tmp1.append(tmp)
    
        return jsonify(str(tmp1))