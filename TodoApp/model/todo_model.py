import datetime
from flask import request, jsonify
from model.auth_model import  auth_model
from flask import jsonify, make_response
from app import db, cursor

obj = auth_model()

def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        
        user_id = obj.verify_token(token)
        if not user_id:
            return jsonify({'message': 'invalid user'})
        return func(user_id, *args, **kwargs)
    return wrapper

class todo_model():
    
    def todo_getall_model(data):
        id = data['id']
        cursor.execute("SELECT title, description FROM todo WHERE id = %s", (id))
        result = cursor.fetchall()
        if len(result) > 0:
            return make_response({"message": result}, 200)
        else:
            return make_response({"message": "No todos found"}, 404)
        
    def todo_addone_model(data):
        title = data['title']
        description = data['description']
        user_id = user_id
        createdAt = datetime.now()
        query = "INSERT INTO todo (title, description, user_id, createdAt) VALUES (%s, %s, %s, %s)"
        values = (title, description, user_id, createdAt,)

        cursor.execute(query, values)
        return make_response({"message": "todo created successfully"}, 200)
    
    def todo_updateone_model(data):
        id = data['id']
        title = data['title']
        description = data['description']
        if title:
            query = "UPDATE todo SET title = %s WHERE id = %s"
            values = (title, id,)
        elif description:
            query = "UPDATE todo SET description = %s WHERE id = %s"
            values = (description, id,)

        cursor.execute(query, values)

        if cursor.rowcount>0:
            return make_response({"message": "todo updated successfully"}, 201)
        else:
            return make_response({"message": "Nothing to update"}) 
        
    def todo_iscompleted_model(data):
        id = data['id']
        query = "SELECT createdAt from todo WHERE id = %s"
        value = (id,)

        res = cursor.execute(query, value)
        
        current_time = datetime.now()
        time_limit = current_time - datetime.timedelta(hours=24)

        if(res <= time_limit ):
            cursor.execute("UPDATE todo SET isCompleted = '1' WHERE id= %s", (id))
            return make_response({'message': 'todo task completed'})
        else:
            return make_response({'message': 'todo task not completed'})
            
    def todo_deleteone_model(data):
        id = data['id']

        query = "UPDATE todo SET isArchived = '1' WHERE id = %s"
        values = (id,)
            
        cursor.execute(query, values)
        return make_response({"message": "todo deleted successfully"}, 200)

