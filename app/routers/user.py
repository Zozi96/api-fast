from typing import List
from fastapi import APIRouter, HTTPException, Response, Cookie, Depends, status
from fastapi.security import HTTPBasicCredentials, OAuth2PasswordRequestForm
from app.settings.security import access_token, get_current_user
from app.schemas.review import ReviewResponseModel
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

# Login a traves de cookie
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

# Login con JWT
@router.post('/authentication')
async def authenticate(form_data: OAuth2PasswordRequestForm = Depends()):
    user = User.select().where(User.username == form_data.username).first()

    # Verificando si el usuario existe o es invalido
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    # Validando contraseña
    if user.password != User.create_password(password=form_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    return {
        'access_token': access_token(form_data.username),
        'token-type': 'Bearer'
    }

@router.get('/access_denied')
async def saludo(user: str = Depends(get_current_user)):
    print(user)
    return {
        'message': 'Hello}!'
    }