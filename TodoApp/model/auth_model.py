from flask import app, jsonify, make_response
from flask_jwt_extended import create_access_token, decode_token, get_jwt_identity
import jwt
from app import db, cursor

class auth_model():
    def auth_login_model(self,data):
        new_email= data['email']
        new_password = data['password']

        query = "SELECT id FROM table1 WHERE email = %s AND password = %s"
        values = (new_email, new_password,)

        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            access_token = create_access_token(identity=new_email)
            return make_response(access_token=access_token), 200
        else:
            return jsonify({"message": "invalid credentials"}), 401
        
    def verify_token(token):
        try:

            decoded_token = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
            user_id = decoded_token['identity']
            return user_id
        except jwt.ExpiredSignatureError:
            return jsonify({'Message': 'token expired'})
        except jwt.InvalidTokenError:
            return jsonify({'message': 'invalid token'})
        
        
    
        