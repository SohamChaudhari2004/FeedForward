from app.models import mongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask import current_app


'''
Class for user reg
 user login
 finding user by id or by email
'''

class User:

    def __init__(self, username, email,password):
        self.username = username
        self.email = email
        self.password = password 

    @staticmethod
    def register(username , email, password):
        ''' hash the saved password first then add the user '''
        hashed_password  = generate_password_hash(password)

        user_data = {
            "username" : username,
            "email": email,
            "password": hashed_password
        }

        mongo.db.users.insert_one(user_data)


    @staticmethod
    def login(email, password):
        ''' login using email and password and return a jwt token'''

        user  = mongo.db.users.find_one({"email": email})
        if user and check_password_hash(user["password"], password):
            ''' create and return the access token'''
            access_token = create_access_token(identity=str(user["_id"]))

            return access_token

        return None

    
    @staticmethod
    def find_user_by_id(user_id):
        return mongo.db.users.find_one({'_id': ObjectId(user_id)})

    @staticmethod
    def find_user_by_email(email):
        return mongo.db.users.find_one({"email": email})
    
    

    @staticmethod
    def get_all():
        # Fetch all users from the "users" collection
        return list(mongo.db.users.find({}, {"password": 0}))