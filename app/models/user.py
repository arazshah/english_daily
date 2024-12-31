from flask_login import UserMixin
from app import db


class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.full_name = user_data['full_name']
        self.email = user_data['email']
        self.username = user_data['username']
        self.password = user_data['password']
        self.score = user_data.get('score', 0)
        self.is_admin = user_data.get('is_admin', False)

    @staticmethod
    def get(user_id):
        user_data = db.users.find_one({'_id': user_id})
        if user_data:
            return User(user_data)
        return None

    @staticmethod
    def find_by_username(username):
        user_data = db.users.find_one({'username': username})
        if user_data:
            return User(user_data)
        return None

    @staticmethod
    def create(full_name, email, username, password, is_admin=False):
        user_data = {
            'full_name': full_name,
            'email': email,
            'username': username,
            'password': password,
            'score': 0,
            'is_admin': is_admin
        }
        result = db.users.insert_one(user_data)
        return User(db.users.find_one({'_id': result.inserted_id}))
