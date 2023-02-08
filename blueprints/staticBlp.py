from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request, jsonify, render_template,redirect

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

        spoof_proof_data={}
        li = [  'phone_number',
            'first_name',
            'last_name',
            'institute',
            'degree',
            'branch',
            'graduate_year',
            'hash']

        for i in li:
            if data[i]:
                spoof_proof_data[i] = data[i]
        spoof_proof_data['stage_two'] = 1
        # print(spoof_proof_data)

        res = update_user_details(spoof_proof_data)
        if res == -1:
            return { 'description' : "Please login & try again !"}  
        return redirect("/")

@staticBlp.route("/register")
class FindEvent(MethodView):
    def get(self, event_id):
        return jsonify(Events.getSingleEvent(event_id))

    def post(self):
        event = Events(request.get_json())
        db.session.add(event)
        db.session.commit()
        return 'ss'
