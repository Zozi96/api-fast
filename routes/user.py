from fastapi import HTTPException
from models.user import User
from schemas.users import UserSchema


async def create_user(user: UserSchema):
    if User.select().where(User.username == user.username).exists():
        return HTTPException(409, 'El username ya se encuentra en uso')

    hash_password = User.create_password(password=user.password)

    user = User.create(
        username=user.username,
        password=hash_password,
    )
    return {
        'data': user.username,
        'message': 'Usuario creado correctamente'
    }
