from app import mysql


class SignUp(mysql.Model):
    __tablename__ = 'sign_up'

    id = mysql.Column(mysql.String, primary_key=True)
    email = mysql.Column(mysql.String)
    password = mysql.Column(mysql.String)
    user_id = mysql.Column(mysql.String)
