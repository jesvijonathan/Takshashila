from flask import Blueprint, request

from models import Users

from controllers.userController import createUser

userRoute = Blueprint("userRoute", __name__, url_prefix='/api')


@userRoute.route("/user", methods=['GET', 'POST'])
def user():
    if (request.method == 'POST'):
        user = Users(request.json)
        return user
