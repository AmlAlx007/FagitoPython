from flask_jwt import jwt_required


@jwt_required()
def list_item():
    return "<h1>Items Listed</h1>"
