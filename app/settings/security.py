import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'aVUp2HhGJmbbRMpRkvJjBW'

def create_token(username):
    data = {
        'username': username, # payload
        'exp': datetime.now() + timedelta(minutes=30) # expires in 30 minutes
    }
    return jwt.encode(data, SECRET_KEY, algorithm='HS256')
