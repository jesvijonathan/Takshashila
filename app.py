# pylint: disable=unused-import
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql:///uhf2k0slsnu7bmyb:eOn7jbeFcvkIacBucq4J@bodkrvfvmjntqymqaawg-mysql.services.clever-cloud.com:3306/bodkrvfvmjntqymqaawg'

db = SQLAlchemy(app)


class Registration(db.Model):
    registration_id = db.Column(db.Integer, nullable= False, primary_key= True)
    user_id = db.Column(db.Integer, nullable= False)
    event = db.Column(db.String(100), nullable= False)
    batch = db.Column(db.String(100), nullable= False)
    
@app.route('/', methods=['POST'])
def index():
    pass




if __name__ == "__main__":
    app.run(debug=True)
