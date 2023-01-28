from flask import Blueprint

from models.userModel import Users

from controllers.userController import createUser

userRoute = Blueprint("userRoute", __name__, url_prefix='/api')

@userRoute.route("/", methods=['GET','POST'])
def do_get():
    return Users.getAllUsers()