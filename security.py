from app.models.SignUp import *
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    print("hhe")
    result = SignUp.find_all()
    for val in result:
        if safe_str_cmp(val.email, username):
            if safe_str_cmp(val.password, password):
                return val
    return None


def identity(payload):
    result = SignUp.find_all()
    user_id = payload['identity']
    for val in result:
        if safe_str_cmp(val.email, user_id):
            return user_id
    return None
