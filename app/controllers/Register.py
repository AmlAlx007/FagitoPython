from flask import request
from app import db
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL


def signup():
    request_data = request.get_json()
    myDB = URL(drivername='mysql', username='admin', password='fAgitod3v', host='fagitodev.cw0t204dkdrj.eu-west-1.rds.amazonaws.com', database='fagito')
    engine = create_engine(name_or_url = myDB)
    connection = engine.connect()

    query = 'SELECT * FROM sign_up'

    result = connection.execute(query)
    for val in result:
        print(val)
    return "hello"


def login():
    return '<h1>Login!</h1>'
