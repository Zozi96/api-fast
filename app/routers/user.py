from app.schemas.review import ReviewResponseModel
from typing import List
from fastapi import APIRouter, HTTPException, Response, Cookie
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
    response.set_cookie(key='user_id', value=user.id)  # TOKEN    return user


@router.get('/reviews', response_model=List[ReviewResponseModel])
async def get_reviews(user_id: int = Cookie(None)):
    user = User.select().where(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            404,
            'El usuario no existe'
        )
    return [user_review for user_review in user.reviews]
