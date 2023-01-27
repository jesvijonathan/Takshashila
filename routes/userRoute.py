from flask import Blueprint

from models.userModel import Users

userRoute = Blueprint("userRoute", __name__, url_prefix='/api')

@userRoute.route("/")
def do_get():
    return Users.getAllUsers()