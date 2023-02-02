
from flask import Flask, jsonify, request, render_template, redirect, url_for, make_response
from flask_mail import *
from flask_restful import Resource, Api
import random

import hashlib
import uuid

import json

from mysql import connector

import random

app = Flask(__name__) 
api = Api(app)

system_email = "jesvijonathan.aids2020@citchennai.net"
system_ps = "happysunday"
domain = "127.0.0.1"

mail = Mail(app)  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465      
app.config["MAIL_USERNAME"] = system_email
app.config['MAIL_PASSWORD'] = system_ps
app.config['MAIL_USE_SSL'] = True  
mail = Mail(app)


# To send same text or html element to multiple or single recipient
def send_email(data,from_db=False, text="", body_text="", html_template=None):
    all_email = []

    if from_db == True:
        for i in data:
            all_email.append(i["email"])
    else:
        if type(data) == "list":
            for i in data:
                all_email.append(i)
        else:
            all_email.append(data)


    msg = Message(
                 text,
                 sender=system_email,
                 recipients=all_email
             )
    
    msg.body = str(text)

    if html_template != None:
        msg.html = render_template(html_template, text=text, body_text=body_text)
    else:
        msg.html = body_text

    mail.send(msg)

    return ("Sent email to " + str(all_email))


# To send verification links to multiple users based of a data (user model data) dictionary
def send_verification_email(data):
    text= "Confirm your email address"
    
    all_user_email = []

    for user in data:
        
        all_user_email.append(user["email"])
        Hash = str(user["phone_number"])

        msg = Message(
                 text,
                 sender=system_email,
                 recipients=[user["email"]]
             )
    
        msg.body = str(text)
    
        msg.html = render_template('verify_link.html',
    
        email=user["email"],
        first_name=user["first_name"],
        hash=Hash,
        domain=domain
        )

        mail.send(msg)
    
        msg0= "hidden : " + domain+"/registration_auth_link/"+Hash

        return render_template("verification_pending.html",val="Email Verification",msg="We have sent a verification link to your email address : ", email=all_user_email, msg2="You can ", msg3=" after verification..", msg0=msg0)


@app.route('/registration_auth_link/<Hash>')
def registration_auth(Hash=""):
    if Hash == "":
        return "no hash provided !"
    #logic to check hash with db and verify the user exists
    return Hash


@app.route("/")
def trigger_sample_test():
    # create a sample user data dict (ex: data from usermodels)
    data1 = {
        'id':1239817923871,
        'email':"jesvi22j@gmail.com",
        'password':'qwerty',
        'phone_number':7010493945,
        'first_name':"Jesvi",
        'last_name':"Jonathan",
        'institute':"",
        'degree':"",
        'branch':"",
        'graduate_year':"",
        'type':"",
        'qr_id':"",
        'google_id':"",
            }
    
    data2 = {
        'id':1212317923871,
        'email':"jesvi22jonathan@gmail.com",
        'password':'qwertys',
        'phone_number':9487868449,
        'first_name':"Jesvi",
        'last_name':"",
        'institute':"",
        'degree':"",
        'branch':"",
        'graduate_year':"",
        'type':"",
        'qr_id':"",
        'google_id':"",
            }
    
    data = [data1,data2]

    test_type = 1
    # 1 for testong verification amil system, 2 for sendning custom email
    
    if test_type ==1:
        return send_verification_email(data)
    elif test_type == 2:
        return send_email(data, from_db=True, text="Subject", body_text="Body Text", html_template=None)


if __name__ == '__main__': 
    app.run(debug=True)