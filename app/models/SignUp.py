from app import db


class SignUp(db.Model):
    __tablename__ = 'sign_up'

    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    user_id = db.Column(db.String)
