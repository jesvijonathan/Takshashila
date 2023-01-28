from flask import Blueprint, request

from controllers.userController import createUser

userRoute = Blueprint("userRoute", __name__, url_prefix='/api')


@userRoute.route("/user", methods=['GET', 'POST'])
def user():
    if (request.method == 'POST'):
        return createUser(request.json)
