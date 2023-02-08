from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request, jsonify, render_template

from database import db
from database import EventRegistration
from database import Events, Users

import os

from . import loginBlp

from controllers.userController import update_user_details
 
# from controllers.userController import createUser

staticBlp = Blueprint("staticBlp", __name__, url_prefix='/')

auth_pop = int(os.getenv('AUTH_POPUP'))

@staticBlp.route("/nig")
def nig():
    return render_template("oauth_redirect_home.html", redirect="/login",mini="0")

@staticBlp.route("/login")
class EventRegistration(MethodView):
    def get(self):

        if auth_pop == 1:
            return render_template("login.html", js= ("javascript:poptasticopener('" + loginBlp.login_auth_url() + "');"))
        return render_template("login.html", js=loginBlp.login_auth_url())

@staticBlp.route("/user_details")
class EventRegistration(MethodView):
    def get(self): 
        return render_template("user_details.html")
    
    def post(self):
        data = request.form
        # spoof_proof_data = {
        #     'phone_number':data.get('phone_number', 0),
        #     'first_name':data.get('first_name', None),
        #     'last_name':data.get('last_name', None),
        #     'institute':data.get('institute', None),
        #     'degree':data.get('degree', None),
        #     'branch':data.get('branch', None),
        #     'graduate_year':data.get('graduate_year', 0),
        #     'hash':data.get('hash', None)
        # }
        # print(spoof_proof_data)        
        
        res = update_user_details(data)
        if res == -1:
            return { 'description' : "user does not exists !"}

        Users.query.filter_by(hash=data["hash"]).first()

        return "kk"
        

@staticBlp.route("/register")
class FindEvent(MethodView):
    def get(self, event_id):
        return jsonify(Events.getSingleEvent(event_id))

    def post(self):
        event = Events(request.get_json())
        db.session.add(event)
        db.session.commit()
        return 'ss'
