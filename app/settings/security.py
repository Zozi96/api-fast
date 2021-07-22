import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = 'aVUp2HhGJmbbRMpRkvJjBW'


def access_token(username):
    data = {
        'username': username,  # payload
        'exp': datetime.utcnow() + timedelta(days=10)  # expires in 30 minutes
    }
    return jwt.encode(data, SECRET_KEY, algorithm='HS256')


def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.exceptions.ExpiredSignatureError:
        return None


def oauth2_schema(endpoint: str):
    return OAuth2PasswordBearer(endpoint)


def get_current_user(token: str = Depends(oauth2_schema('/users/authentication'))):
    data = decode_token(token)
    if data and data.get('username') and data.get('exp'):

        if datetime.fromtimestamp(data.get('exp')) > datetime.utcnow():
            return data.get('username')

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Token has expired',
        headers={'WWW-Authenticate': 'Bearer'}
    )
