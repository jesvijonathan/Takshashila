from flask_smorest import Blueprint
from flask.views import MethodView
from flask import request, jsonify, render_template,redirect, url_for,make_response

import json

from database import db
from database import EventRegistration
from database import Events, Users, Verification

from controllers.userController import createUser
import os

from . import loginBlp

from passlib.hash import pbkdf2_sha256

from controllers.userController import update_user_details ,update_user_details_veri


from utils.email_system import send_verification_email, send_email
 
# from controllers.userController import createUser

staticBlp = Blueprint("staticBlp", __name__, url_prefix='/')
# int(os.getenv('AUTH_POPUP'))
auth_pop = 0
domain="https://www.cittakshashila.in/"

@staticBlp.route("/profile/<hash>")
# @cache.cached(timeout=2)
def profile(hash=""):
    if hash == "":
        return "error"
    raw_data = Users.findExistingUserByHash(hash=hash).__dict__.items()
    data = {}

    for j, k in raw_data:
        data[j] = str(k) 
    print(data)

    return render_template("profile.html", 
                           first_name= data.get("first_name", None), 
                           last_name= data.get("last_name", None), 
                           email= data.get("email"),
                           phone_number= data.get("phone_number", None),
                           institution=data.get("institute", None),
                           degree= data.get("degree", None),
                           branch= data.get("branch", None),
                           graduate_year=data.get("graduate_year", None),
                           acc_type=data.get("type", 'student'),
                           qr_id=data.get("qr_id", None),   
                           user_qr=data.get("user_qr", None),
                           updated_at=data.get("created_at",None),
                           )


"""
multi layer sql object data


raw_data = Users.findExistingUserByHash(hash=hash)
    tmp = []
 
    tmp.append(raw_data.__dict__.items()) 
    data = {}
    for i in tmp:
        for j, k in i:
            data[j] = str(k) 

    return jsonify(data)
"""
# @staticBlp.route("/login")
# class authlogin(MethodView):
#     def get(self):
#         return redirect("/")

@staticBlp.route("/login")
class authlogin(MethodView):
    def get(self):

        # if auth_pop == 1:
        #     return render_template("login.html", js= ("javascript:popstasticopener('" + loginBlp.login_auth_url() + "');"))
        return render_template("login.html", js=loginBlp.login_auth_url())
    
    def post(self):
        data = request.form
        user_in_db = None
        user_password = None
        user_db_password = None

        if (not ( user_in_db := Users.findExistingUser(data["email"]))) or user_in_db.verified == '0': 
            return render_template('login.html', error=1)
        
        else:
            if user_password := data['password']:
                
                if (user_in_db.password) and (pbkdf2_sha256.verify(user_password, user_in_db.password)):
                    resp = None
                    redirect_url=domain

                    if not user_in_db.stage_two:
                        redirect_url=domain+"user_details"  

                    resp = make_response(redirect(redirect_url))
                        #resp = make_response(render_template("oauth_redirect_home.html", redirect=redirect_url))   
                    

                    resp.set_cookie('oauth_redirect', redirect_url, secure=True, samesite='Lax') 
                    resp.set_cookie('logged_In', "true", secure=True, samesite='Lax') 
                    resp.set_cookie('first_name', '', secure=True, samesite='Lax',expires=0) 
                    resp.set_cookie('last_name', '', secure=True, samesite='Lax', expires=0) 
                    resp.set_cookie('phone', '', secure=True, samesite='Lax',expires=0) 
                    resp.set_cookie('email',data["email"], secure=True, samesite='Lax')
                    resp.set_cookie('hash', user_in_db.hash, secure=True, samesite='Lax')
                    return resp
                else:
                    return render_template('login.html', error=2)
            else:
                return render_template('login.html', error=0)
            

 
@staticBlp.route("/create_account")
class authlogin(MethodView):
    def get(self):
        
        return render_template("create_account.html",js=loginBlp.login_auth_url())
    
    def post(self):
        data = request.form.to_dict()
        if data["email"] and data["password"]:
                if (not (uss := createUser(data))):
                    print(Users.findExistingUser(data["email"]).verified)
                    if Users.findExistingUser(data["email"]).verified == '1':
                        return {"message": "Email already exists.."}, 409 

                
                return send_verification_email(data) 
        else:
            return {'description':"stupid data"}
        return data
    
@staticBlp.route('/registration_auth_link/<Hash>')
def registration_auth(Hash=""):
    if Hash == "":
        return "no hash provided !"
    if not (data_veri := Verification.findExistingUserByHash(Hash)):
        return "invalid"
    data= {
        'email': data_veri.email,
        'verified':'1',
    }
    
    # print(data.email, Users.query.filter_by(email=data.email).first() )
    if not ( user_db_data:= update_user_details_veri(data=data)):
        return "invalid 2"
    
    Verification.query.filter_by(email=user_db_data.email).delete() 
    db.session.commit()
    
    resp = None
    redirect_url=domain

    if not user_db_data.stage_two:
        redirect_url=domain+"user_details"  

    resp = make_response(redirect(redirect_url))
        #resp = make_response(render_template("oauth_redirect_home.html", redirect=redirect_url))   
    print(user_db_data)
    resp.set_cookie('oauth_redirect', redirect_url, secure=True, samesite='Lax') 
    resp.set_cookie('logged_In', "true", secure=True, samesite='Lax') 
    resp.set_cookie('first_name', user_db_data.first_name, secure=True, samesite='Lax') 
    resp.set_cookie('last_name', str(user_db_data.last_name), secure=True, samesite='Lax') 
    resp.set_cookie('phone', user_db_data.phone_number, secure=True, samesite='Lax')  
    resp.set_cookie('user_details', '1', secure=True, samesite='Lax') 
    resp.set_cookie('email',data["email"], secure=True, samesite='Lax')
    resp.set_cookie('hash', user_db_data.hash, secure=True, samesite='Lax')


    return resp

@staticBlp.route("/user_details")
class EventRegistration(MethodView):
    def get(self): 
        return(render_template("user_details.html"))
    
    
    def post(self):
        data = request.form.to_dict()

        spoof_proof_data={}
        li = [  'phone_number',
            'first_name',
            'last_name',
            'institute',
            'degree',
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
        

        resp = make_response(redirect("/")) 
        resp.set_cookie('user_details', '1', secure=True, samesite='Lax') 
        return resp

@staticBlp.route("/register")
class FindEvent(MethodView):
    def get(self, event_id):
        return jsonify(Events.getSingleEvent(event_id))

    def post(self):
        event = Events(request.get_json())
        db.session.add(event)
        db.session.commit()
        return 'ss'
