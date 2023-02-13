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

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET')
app.config["API_TITLE"] = "TK2023 Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"



system_email = "your email (check less secure option, google it)"
system_ps = "your password"
domain = "127.0.0.1:5000" #local host

mail = Mail(app)  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465      
app.config["MAIL_USERNAME"] = os.getenv('SECRET')
app.config['MAIL_PASSWORD'] = system_ps
app.config['MAIL_USE_SSL'] = True  
mail = Mail(app)

# cache = Cache(config={'CACHE_TYPE': 'simple'})
# cache = Cache(app)

api = Api(app)
Database(app)
JWT(app)


@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
# @cache.cached(timeout=2)
def index():
    return render_template("index.html")


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
    app.run(debug=True)
