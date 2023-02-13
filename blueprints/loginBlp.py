from flask_smorest import Blueprint
from flask.views import MethodView
from flask import make_response

import os
import pathlib
import requests

from flask import session, abort, redirect, request, render_template
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

from controllers.userController import createUser_oauth

loginBlp = Blueprint("loginBlp", __name__, url_prefix='/auth')

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
auth_pop = int(os.getenv('AUTH_POPUP')) 

GOOGLE_CLIENT_ID = "562058780483-q59qv7347cgqujgebrsf15n6b0u8uhmq.apps.googleusercontent.com"
client_secrets_file = os.path.join(
    pathlib.Path(__file__).parent, "../client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/auth/callback"
)

def login_auth_url():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return authorization_url

@loginBlp.route("/")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    # return redirect(authorization_url)
    return redirect(authorization_url)

@loginBlp.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)
    if not session["state"] == request.args["state"]:
        abort(500)

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(
        session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    data = {
        'email':id_info['email'],
        'first_name':id_info.get('given_name', None),
        'last_name':id_info.get('family_name', None),
        'google_id':id_info['at_hash'],
    }

    user_db_data = createUser_oauth(data)

    resp = None
    redirect_url="http://127.0.0.1:5000/"
    
    if not user_db_data.stage_two:
        redirect_url="http://127.0.0.1:5000/user_details"  
        f =1

    if auth_pop == 1:
        resp = make_response(render_template("oauth_redirect_home.html", redirect=redirect_url, mini=auth_pop))
        
    else:
        resp = make_response(redirect(redirect_url))
        #resp = make_response(render_template("oauth_redirect_home.html", redirect=redirect_url))   
    
    resp.set_cookie('oauth_redirect', redirect_url, secure=True, samesite='Lax') 
    resp.set_cookie('logged_In', "true", secure=True, samesite='Lax') 
    if f ==1:resp.set_cookie('user_details', '', secure=True, samesite='Lax') 
    resp.set_cookie('first_name', id_info.get("given_name", ""), secure=True, samesite='Lax') 
    resp.set_cookie('last_name', id_info.get("family_name", ""), secure=True, samesite='Lax') 
    resp.set_cookie('email', id_info["email"], secure=True, samesite='Lax')
    resp.set_cookie('hash', user_db_data.hash, secure=True, samesite='Lax')

    return resp