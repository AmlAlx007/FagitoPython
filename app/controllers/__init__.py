import os
from flask import Blueprint, current_app

from app.controllers.Register import signup as signup
from app.controllers.Register import login as login
from app.controllers.ListItems import list_item as list_item


user_blueprints = Blueprint('register', 'api', template_folder=None)
user_blueprints.add_url_rule('/signup', view_func=signup, methods=['POST'])
user_blueprints.add_url_rule('/login', view_func=login, methods=['GET'])
user_blueprints.add_url_rule('/items', view_func=list_item, methods=['GET'])

