import os

from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, redirect, url_for, session, make_response, request

from flask_smorest import Api
from flask_caching import Cache
from flask_mail import Mail
from flask_dance.contrib.google import make_google_blueprint, google


from utils.jwt import JWT
from database import Database, db

from blueprints.authBlp import authBlp
from blueprints.loginBlp import loginBlp
from blueprints.feedBackBlp import feedBackBlp
from blueprints.staticBlp import staticBlp

from blueprints.eventBlp import eventBlp

from utils.email_system import email
from controllers.verificationController import *
from sqlalchemy.orm import Session



import json

load_dotenv()

project_folder = os.path.expanduser('~/my-project-dir')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))


app = Flask(__name__, static_url_path='/')
app.app_context().push()

app.secret_key = os.getenv('SECRET')
app.config["API_TITLE"] = "TK2023 Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"

app.config['SQLALCHEMY_POOL_RECYCLE'] = 280
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
app.config['SQLALCHEMY_POOL_PRE_PING'] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.teardown_request
def session_clear(exception=None):
    db.session.close()
    db.session.remove()
    

try:
    os.mkdir("/home/takshashila/Takshashila-2023-Backend/static/users")
except:
    print("user qr already exists")


# cache = Cache(config={'CACHE_TYPE': 'simple'})
# cache = Cache(app)

api = Api(app)
Database(app)
JWT(app)
email(app)


@app.before_first_request
def create_tables():
    db.create_all()




@app.route("/")
# @cache.cached(timeout=2)
def index():
    return render_template("index.html")

@app.route("/events")
# @cache.cached(timeout=2)
def events():
    return render_template("events.html")

@app.route("/events#/<text>")
# @cache.cached(timeout=2)
def nig():
    return render_template("events.html")


blueprint = make_google_blueprint(
    client_id="562058780483-q59qv7347cgqujgebrsf15n6b0u8uhmq.apps.googleusercontent.com",
    client_secret="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",
    redirect_url="https://takshashila.pythonanywhere.com/google_login",
    scope = 'openid https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile'
)

app.register_blueprint(blueprint, url_prefix="/login")

from controllers.userController import createUser_oauth

auth_pop = 0
domain = "http://takshashila.pythonanywhere.com/"
# server_url =os.getenv('SERVER_URL')
server_url = "http://takshashila.pythonanywhere.com/"

@app.route("/google_login")
def google_():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    email = resp.json()["email"]

    res_data= resp.json()

    data = {
        'email':res_data.get('email', None),
        'first_name':res_data.get('given_name', None),
        'last_name': res_data.get('family_name', None),
        'google_id':res_data.get('id', None)
    }

    user_db_data = createUser_oauth(data)

    resp = None
    redirect_url=domain
    f =0
    if not user_db_data.stage_two:
        redirect_url=domain+"user_details"
        f =1

    if auth_pop == 1:
        resp = make_response(render_template("oauth_redirect_home.html", redirect=redirect_url, mini=auth_pop))

    else:
        resp = make_response(redirect(redirect_url))
        #resp = make_response(render_template("oauth_redirect_home.html", redirect=redirect_url))

    resp.set_cookie('oauth_redirect', redirect_url, secure=True, samesite='Lax')
    resp.set_cookie('logged_In', "true", secure=True, samesite='Lax')
    if f ==1:resp.set_cookie('user_details', '', secure=True, samesite='Lax')
    resp.set_cookie('first_name', res_data.get('given_name'), secure=True, samesite='Lax')
    resp.set_cookie('last_name', res_data.get('family_name', ""), secure=True, samesite='Lax')
    resp.set_cookie('email', res_data.get('email', ""), secure=True, samesite='Lax')
    resp.set_cookie('hash', user_db_data.hash, secure=True, samesite='Lax')

    return resp

    return f"Logged in as {email}"



@app.errorhandler(404)
# @cache.cached(timeout=2)
def page_not_found(e):
    return jsonify(error=str(e)), 404
    return render_template('404.html', error=e, console_print=e), 404


@app.route('/edit_events')
#/home/takshashila/Takshashila-2023-Backend/static
def edit():
    with open('./static/events.json', 'r') as f:
        data = json.load(f)
    return render_template('edit.html', data=json.dumps(data, indent=4, ))


@app.route('/update', methods=['POST'])
def update():
    new_data = request.json
    with open('./static/events.json', 'w') as f:
        json.dump(new_data, f)
    return jsonify(success=True)


api.register_blueprint(staticBlp)
api.register_blueprint(authBlp)
api.register_blueprint(eventBlp)
api.register_blueprint(loginBlp)
api.register_blueprint(feedBackBlp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)

