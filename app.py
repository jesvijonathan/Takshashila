from utils.jwt import JWT
from database import Database, db
from blueprints.authBlp import authBlp
from blueprints.eventBlp import eventBlp
import os
from dotenv import load_dotenv
from flask import Flask
from flask_smorest import Api

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

if __name__ == '__main__':
    app.run(debug=True)
