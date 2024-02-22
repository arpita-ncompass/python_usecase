from app import app
from model.user_model import user_model
from flask import request

obj3= user_model()

@app.route('/users/getall')
def user_getall_controller():
    return obj3.user_getall_model()

@app.route('/users/addone', methods=['POST'])
def user_addone_controller():
    return obj3.user_addone_model(request.get_json())

@app.route('/users/updateone', methods=['PUT'])
def user_updateone_controller():
    return obj3.user_updateone_model(request.get_json())

@app.route('/users/deleteone', methods=['DELETE'])
def user_deleteone_controller():
    return obj3.user_deleteone_model(request.get_json())




