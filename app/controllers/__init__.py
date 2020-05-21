import os
from flask import Blueprint, current_app

from app.controllers.Register import signup
from app.controllers.Register import login


user_blueprints = Blueprint('register', 'api')
user_blueprints.add_url_rule('/signup', view_func=signup(), methods=['POST'])
user_blueprints.add_url_rule('/login', view_func=login(), methods=['GET'])
