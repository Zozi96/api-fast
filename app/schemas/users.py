from pydantic import BaseModel, validator
from . import ResponseModel


class UserSchema(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError(
                'La longitud debe encontrarse entre 3 y 50 caracteres'
            )
        return username


class UserResonseModel(ResponseModel):
    id: int
    username: str
