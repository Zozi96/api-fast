from fastapi import APIRouter, HTTPException
from ..models.user import User
from ..schemas.users import UserResonseModel, UserSchema

router = APIRouter(prefix='/users')


@router.post('/create', response_model=UserResonseModel)
async def create_user(user: UserSchema):
    if User.select().where(User.username == user.username).exists():
        return HTTPException(409, 'El username ya se encuentra en uso')

    hash_password = User.create_password(password=user.password)

    return User.create(
        username=user.username,
        password=hash_password,
    )
