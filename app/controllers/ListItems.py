from flask import  request
from app.models.JwtEncoder import decode_auth_token
import jwt


def list_item():
    try:
        decode_auth_token(request.headers['Authorization'].split(" ")[1])
        return "Items Listed"
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
