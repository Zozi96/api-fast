import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = 'aVUp2HhGJmbbRMpRkvJjBW'


def access_token(username):
    data = {
        'username': username,  # payload
        'exp': datetime.now() + timedelta(minutes=30)  # expires in 30 minutes
    }
    return jwt.encode(data, SECRET_KEY, algorithm='HS256')


def oauth2_schema(endpoint: str):
    return OAuth2PasswordBearer(tokenUrl=endpoint)
