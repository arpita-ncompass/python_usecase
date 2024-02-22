from app import app
from model.auth_model import auth_model
from flask import request

obj2 = auth_model()

@app.route('/users/login', methods=['POST'])
def auth_login_controller():
    return obj2.auth_login_model(request.get_json())
