
from flask import Flask, render_template
from flask_mail import *
from flask_restful import Api
import os
from utils.jwt import generate_hash 

from controllers.verificationController import *

 

domain = os.getenv('SERVER_URL') 
system_email = os.getenv('SYSTEM_EMAIL')
system_email_password  = os.getenv('SYSTEM_EMAIL_PASSWORD')

mail = None

# define variables
class email():
    def __init__(self,app):
        global mail
        app.config["MAIL_SERVER"]='smtp.gmail.com'  
        app.config["MAIL_PORT"] = 465      
        app.config["MAIL_USERNAME"] = system_email
        app.config['MAIL_PASSWORD'] = system_email_password
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
def send_verification_email(data, id=""):
    text= "Confirm your email address"
     

    if (alt_hash := create_verification(data)):
        render_template("message.html", title="Error", 
                message_1=("Sorry, we ran into an error. Please try again !"))

    user_email = data["email"]
    msg = Message(
             text,
             sender=system_email,
             recipients=[user_email]
         )


    msg.body = str(text)

    msg.html = render_template('verify_link.html',


    title="Email Verification",
    email=user_email,
    first_name=data["first_name"],
    link= str(domain + "/registration_auth_link/"  + str(alt_hash)) 
    )
    mail.send(msg)

    
    

    return render_template("message.html", title="Email Verification", 
                message_1=("We have sent an email verification link to your email address : "), link_1=user_email,
                message_3="You can ", link_3="Login", message_3_1="after verification..",
                message_10="If you don't see it, you may have to chek your spam folder")

    

# @app.route('/registration_auth_link/<Hash>')
# def registration_auth(Hash=""):
#     if Hash == "":
#         return "no hash provided !"
#     #logic to check hash with db and verify the user exists
#     return Hash


# @app.route("/")
# def trigger_sample_test():
#     # create a sample user data dict (ex: data from usermodels)
#     data1 = {
#         'id':1239817923871,
#         'email':"jesvi22j@gmail.com",
#         'password':'qwerty',
#         'phone_number':7010493945,
#         'first_name':"Jesvi",
#         'last_name':"Jonathan",
#         'institute':"",
#         'degree':"",
#         'branch':"",
#         'graduate_year':"",
#         'type':"",
#         'qr_id':"",
#         'google_id':"",
#             }
    
#     data2 = {
#         'id':1212317923871,
#         'email':"jesvi22jonathan@gmail.com",
#         'password':'qwertys',
#         'phone_number':9487868449,
#         'first_name':"Jesvi",
#         'last_name':"",
#         'institute':"",
#         'degree':"",
#         'branch':"",
#         'graduate_year':"",
#         'type':"",
#         'qr_id':"",
#         'google_id':"",
#             }
    
#     data = [data1,data2]

#     test_type = 1
#     # 1 for testong verification amil system, 2 for sendning custom email
    
#     if test_type ==1:
#         return send_verification_email(data)
#     elif test_type == 2:
#         return send_email(data, from_db=True, text="Subject", body_text="Body Text", html_template=None)

 