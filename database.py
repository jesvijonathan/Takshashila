from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
db = SQLAlchemy()

class Database():
    def __init__(self,app):
        app.config["MYSQL_DATABASE_HOST"] = os.getenv("DATABASE_HOST")
        app.config["MYSQL_DATABASE_USER"] = os.getenv("DATABASE_USER")
        app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("DATABASE_PASSWORD")
        app.config["MYSQL_DATABASE_DB"] = os.getenv("DATABASE_DB")
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

        db.init_app(app)