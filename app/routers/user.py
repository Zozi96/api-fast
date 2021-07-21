from fastapi import APIRouter, HTTPException, Response
from fastapi.security import HTTPBasicCredentials
from ..models.user import User
from ..schemas.users import UserResonseModel, UserSchema

router = APIRouter(prefix='/users')


@router.post('/create', response_model=UserResonseModel)
async def create_user(user: UserSchema):
    if User.select().where(User.username == user.username).exists():
        raise HTTPException(
            409,
            'El username ya se encuentra en uso'
        )

    hash_password = User.create_password(password=user.password)

    return User.create(
        username=user.username,
        password=hash_password,
    )


@router.post('/login', response_model=UserResonseModel)
async def login(credentials: HTTPBasicCredentials, response: Response):
    user = User.select().where(
        User.username == credentials.username
    ).first()

    if user is None:
        raise HTTPException(
            404,
            'El usuario no existe'
        )

    if user.password != User.create_password(password=credentials.password):
        raise HTTPException(
            401,
            'El password es incorrecto'
        )
    response.set_cookie(key='user_id', value=user.id)
    return user
