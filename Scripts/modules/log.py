from os import truncate
import database
from config import *
from mysql import connector
from flask import Flask, redirect, url_for, request, render_template

import pickle

def visitor_ip():
    print(request.remote_addr,request.environ['REMOTE_ADDR'])
    pass


def dash_load_data():
    di = None

    try:
        with open('data/users.pkl', 'rb') as f:
            di = pickle.load(f)
        print("user data loaded")
    except:
        print("error laoding")
        #dash_data_res()

    return di



def dash_load_data_guest():
    di = None

    try:
        with open('data/guest.pkl', 'rb') as f:
            di = pickle.load(f)
        print("user data loaded")
    except:
        print("error laoding")
        #dash_data_res()

    return di


def dash_data_res():
    dic = {}

    dic2 = { 'username':'admin', 
    'password':'root', 
    'email':email, 
    'first_name':'administrator', 
    'last_name':'',
    'member':'sudo',}
    
    dic['admin']=dic2

    with open('data/users.pkl', 'wb') as f:
        pickle.dump(dic, f)
    
    print("user data initialize/reseted")


def dash_data_res_guest():
    dic = {}

    dic2 = { 'username':'guest', 
    'password':'guest', 
    'email':'guest_mail@gmail.com', 
    'first_name':'guest', 
    'last_name':'',
    'member':'user',}
    
    dic['guest']=dic2

    with open('data/guest.pkl', 'wb') as f:
        pickle.dump(dic, f)
    
    print("guest data initialize/reseted")


def dash_register(d):   
    dic = dash_load_data()
    ok_list = []

    for y in d:
        for x in dic:
            if y == x:
                print(x,"email already there...")
                return "Username already present.."
            elif dic[x]["email"] == d[y]["email"]:
                print(d[y]["email"], "email already there...")
                return "Email already present.."
            else:
                ok_list.append(y)

    for user in ok_list:
        dic[user]=d[user] 

    try:
        with open('data/users.pkl', 'wb') as f:
            pickle.dump(dic, f)
    except:
        print("error")
        return "Error"
        
    return 1



def dash_register_guest(d):   
    dic = dash_load_data()
    ok_list = []
    del_ = []

    with open('data/guest.pkl', 'rb') as f:
            g = pickle.load(f)

    for y in d:
        for x in dic:
            if y == x:
                print(x,"Username already there...")
                return "Username already present.."
            elif d[y]["email"] == dic[x]["email"]:
                print(d[y]["email"], "email already there...")
                return "Email already present.."
        for z in g:
            if y == z:
                del_.append(g[z])
            elif d[y]["email"] == g[z]["email"]:
                del_.append(g[z])
            else:
                ok_list.append(y)

    for user in del_:
        print(user["username"])
        del g[user["username"]]

    for user in ok_list:
        g[user]=d[user] 

    try:
        with open('data/guest.pkl', 'wb') as f:
            pickle.dump(g, f)
    except:
        print("error")
        return "Error"
        
    return 1


def delete_user(username=None,email=None):
    dic = dash_load_data()

    """
    ok_list = []
    
    for x in dic:
        if username == x:
            print(x,"user found")
        elif email == dic[x]["email"]:
            print("email found")
        else:
            ok_list.append(x)

    for user in ok_list:
        dic[user]=d[user] 
    """
    
    try:
        del dic[username]
        print("User",username,"deleted !")
    except:
        print("Error")

    try:
        with open('data/users.pkl', 'wb') as f:
            pickle.dump(dic, f)
    except:
        print("error")
        return "Error"

    return 1


def delete_guest(username=None,email=None):
    dic = dash_load_data_guest()

    """
    ok_list = []
    
    for x in dic:
        if username == x:
            print(x,"user found")
        elif email == dic[x]["email"]:
            print("email found")
        else:
            ok_list.append(x)

    for user in ok_list:
        dic[user]=d[user] 
    """
    
    try:
        del dic[username]
        print("Guest",username,"deleted !")
    except:
        print("Error")

    try:
        with open('data/guest.pkl', 'wb') as f:
            pickle.dump(dic, f)
    except:
        print("error")
        return "Error"

    return 1


def arrange(u,p,e,fn,ln,m,guest=1):
    d = {}
    d1 = {'username':u, 'password':p, 'email':e, 'firstname':fn, 'lastname':ln, 'member':m }
    d[u]=d1
    return dash_register_guest(d)


def verify(username=None, email=None):
    d = {}
    g = dash_load_data_guest()
    d[username]=g[username]
    delete_guest(username)
    return dash_register(d)

#menu()