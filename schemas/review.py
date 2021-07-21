from . import PeeweeGetterDict, ResponseModel
from pydantic import BaseModel


class MovieRequestModel(BaseModel):
    title: str


class MovieResponseModel(ResponseModel):
    id: int
    title: str


class ReviewRequestModel(BaseModel):
    user: int  # ID del usuario
    movie: int  # ID de la pelicula
    review: str
    score: int


class ReviewResponseModel(ResponseModel):
    movie: int  # ID de la pelicula
    review: str
    score: int
