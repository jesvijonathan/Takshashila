import os
from dotenv import load_dotenv
from flask import Flask
from flask_smorest import Api

from utils.jwt import JWT
from database import Database, db

from blueprints.authBlp import authBlp
from blueprints.loginBlp import loginBlp
from blueprints.feedBackBlp import feedBackBlp

from blueprints.eventBlp import eventBlp

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET')
app.config["API_TITLE"] = "TK2023 Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"

api = Api(app)
Database(app)
JWT(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.register_blueprint(authBlp)
api.register_blueprint(eventBlp)
api.register_blueprint(loginBlp)
api.register_blueprint(feedBackBlp)

if __name__ == '__main__':
    app.run(debug=True)
