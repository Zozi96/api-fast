from models.user import User
from schemas.users import UserSchema


async def create_user(user: UserSchema):
    user = User.create(
        username=user.username,
        password=user.password,
    )
    return user.id
