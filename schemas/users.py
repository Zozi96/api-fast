from pydantic import BaseModel, validator
from . import PeeweeGetterDict


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


class UserResonseModel(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
        gettet_dict = PeeweeGetterDict
