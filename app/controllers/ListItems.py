from flask import  request
from app.models.JwtEncoder import decode_auth_token


def list_item():
    value = decode_auth_token(request.headers['Authorization'].split(" ")[1])
    return value
