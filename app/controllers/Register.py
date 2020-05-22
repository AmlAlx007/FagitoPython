from flask import request
from database import db
from app import app
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from app.models.SignUp import *
from app.models.StudentMail import *


def signup():
    signup_object = SignUp()

    request_data = request.get_json()
    result = SignUp.order_data()
    value = result[result.count() - 1]

    signup_object.sign_up_id = value.sign_up_id[0:2] + str(int(value.sign_up_id[2:]) + 1)

    # checking for an exsisting mail id
    for value in result:
        try:
            if value.email == request_data['email']:
                raise Exception()
        except:
            return {"message": "Email id already exsists !!!"}

    signup_object.email = request_data['email']
    signup_object.password = request_data['password']

    email_domain = request_data['email'].split('@')[1].split('.')[1]
    university_domains = StudenMail.find_all()
    flag = 0
    # checking for the domain
    for domain in university_domains:
        if email_domain == domain.mail_domain:
            signup_object.user_id = "S" + signup_object.sign_up_id[2:]
            flag = 1
            break
    if flag == 0:
        signup_object.user_id = "C" + signup_object.sign_up_id[2:]
    try:
        signup_object.commit_data()
    except:
        return {"message", "An error occured while inserting an item"}, 500

    return "Account created"


def login():
    request_data = request.get_json()

    result = SignUp.find_all()
    for val in result:
        try:
            if val.email == request_data['email']:
                if val.password == request_data['password']:
                    return {"message": "Login Successfully"}, 200
                else:
                    raise Exception()
        except:
            return {"message": "User credentials doesn't match !!!"}, 200

    return {"message": "Account is not registered !!!"}, 200