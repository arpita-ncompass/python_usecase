from flask import Flask
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

try:
    db = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        autocommit=True
    )
    if db.is_connected():
        print("successfully connected to db")
    else:
        print("failed to connect to db")
except mysql.connector.Error as e:
    print('error connecting to database')

cursor = db.cursor(dictionary=True)

from controller import todo_controller,auth_controller
