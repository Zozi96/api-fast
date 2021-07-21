from . import PeeweeGetterDict, ResponseModel
from pydantic import BaseModel, validator


class MovieRequestModel(BaseModel):
    title: str


class MovieResponseModel(ResponseModel):
    id: int
    title: str


class ScoreValidator:
    @validator('score')
    def check_score(cls, score):
        if score < 1 or score > 5:
            raise ValueError(
                'El rango del puntaje es entre 1 y 5'
            )
        return score


class ReviewRequestModel(BaseModel, ScoreValidator):
    user: int  # ID del usuario
    movie: int  # ID de la pelicula
    review: str
    score: int


class ReviewResponseModel(ResponseModel):
    id: int
    movie_id: int  # ID de la pelicula
    review: str
    score: int


class ReviewRequestPutModel(BaseModel, ScoreValidator):
    review: str
    score: int
