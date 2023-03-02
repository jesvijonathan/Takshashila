import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify
from flask_smorest import Api
from flask_caching import Cache
from flask_mail import Mail

from utils.jwt import JWT
from database import Database, db

from blueprints.authBlp import authBlp
from blueprints.loginBlp import loginBlp
from blueprints.feedBackBlp import feedBackBlp
from blueprints.staticBlp import staticBlp

from blueprints.eventBlp import eventBlp

from utils.email_system import email
from controllers.verificationController import *

load_dotenv()

project_folder = os.path.expanduser('~/my-project-dir')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))


app = Flask(__name__, static_url_path='/')
app.secret_key = os.getenv('SECRET')
app.config["API_TITLE"] = "TK2023 Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"

 
try:
    os.mkdir(f"./users/qr")
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


@app.errorhandler(404)
# @cache.cached(timeout=2)
def page_not_found(e): 
    return jsonify(error=str(e)), 404
    return render_template('404.html', error=e, console_print=e), 404



api.register_blueprint(staticBlp)
api.register_blueprint(authBlp)
api.register_blueprint(eventBlp)
api.register_blueprint(loginBlp)
api.register_blueprint(feedBackBlp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)
    
