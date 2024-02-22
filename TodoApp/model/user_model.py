from flask import jsonify, make_response
from app import db, cursor
from cerberus import Validator

class user_model():
    def user_getall_model(self):
        cursor.execute("SELECT * FROM table1")
        result = cursor.fetchall()
        if len(result) > 0:
            return make_response({"message": result}, 200)
        else:
            return make_response({"message": "No data found"}, 404)
        

    def user_addone_model(data):
        new_name = data['name']
        new_email = data['email']
        new_password = data['password']
        query = "INSERT INTO table1 (name, password, email) VALUES (%s, %s, %s)"
        values = (new_name, new_password, new_email,)

        cursor.execute(query, values)
        return make_response({"message": "user created successfully"}, 200)
    
    def user_updateone_model(data):
        id = data['id']
        new_name = data.get('name')
        new_email = data.get('email')
        if new_name:
            query = "UPDATE table1 SET name = %s WHERE id = %s"
            values = (new_name, id,)
        elif new_email:
            query = "UPDATE table1 SET email = %s WHERE id = %s"
            values = (new_email, id,)
            
        cursor.execute(query, values)

        if cursor.rowcount>0:
            return make_response({"message": "user updated successfully"}, 201)
        else:
            return make_response({"message": "Nothing to update"}) 

        
    def user_deleteone_model(data):
        id = data['id']

        query = "DELETE FROM table1 WHERE id = %s"
        values = (id,)
            
        cursor.execute(query, values)
        return make_response({"message": "user deleted successfully"}, 200)