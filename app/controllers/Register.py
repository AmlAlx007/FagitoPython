from flask import request
from database import db
from app import app
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from app.models.SignUp import SignUp


def signup():
    print("hello")
    request_data = request.get_json()
    result = SignUp.find_all()
    for val in result:
        print(val.email)
    return "hello"


def login():
    return '<h1>Login!</h1>'
