import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


mysql = MySQL()


def initialize_extensions(application):
    mysql.init_app(application)
    from app.models.SignUp import SignUp

    db1 = MySQL(application)


def register_blueprints(application):
    from app.controllers import user_blueprints
    application.register_blueprint(user_blueprints)


def create_app(config_filename=None):
    application = Flask(__name__, instance_relative_config=True)
    application.config.from_pyfile(config_filename)
    initialize_extensions(application)
    register_blueprints(application)
    return application


config_filename = os.path.abspath(os.path.dirname(__file__)) + "/../instance/development.cfg"
app = Flask(__name__)
app.config.from_pyfile(config_filename)
db = MySQL(app)