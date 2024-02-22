import flask
from app import app
from model.todo_model import todo_model, token_required
from flask import request

obj1 = todo_model()

@app.route('/todo/getall', methods=['POST'])
@token_required
def todo_getall_controller():
    return obj1.todo_getall_model(request.get_json())

@app.route('/todo/addone', methods=['POST'])
@token_required
def todo_addone_controller():
    return {"a":1}
    # return obj1.todo_addone_model(request.get_json())

# @app.route('/todo/updateone', methods=['PUT'])
# @token_required
# def todo_updateone_controller():
#     return obj1.todo_updateone_model(request.get_json())

# @app.route('/todo/deleteone', methods=['DELETE'])
# def todo_deleteone_controller():
#     return obj1.todo_deleteone_model(request.get_json())

# @app.route('/todo/checktodo', methods= ['POST'])
# def todo_iscompleted_controller():
#     return obj1.todo_iscompleted_model(request.get_json())