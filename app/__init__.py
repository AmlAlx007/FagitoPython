import os
from flask import Flask
from database import db


def initialize_extensions():
    from app.models.SignUp import SignUp
    from app.models.StudentMail import StudenMail


def register_blueprints(application):
    from app.controllers import user_blueprints
    application.register_blueprint(user_blueprints)


def create_app(config_filename=None):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_pyfile(config_filename)
    initialize_extensions()
    register_blueprints(application)
    db.init_app(application)
    return application


config_filename = os.path.abspath(os.path.dirname(__file__)) + "/../instance/development.cfg"
app = Flask(__name__)
app.config.from_pyfile(config_filename)

