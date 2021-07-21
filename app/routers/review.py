from fastapi import APIRouter
from ..models.review import UserReview, Movie
from ..schemas.review import (
    MovieResponseModel, MovieRequestModel, ReviewRequestModel, ReviewResponseModel
)

router = APIRouter(prefix='/reviews')


@router.post('/movies/create', response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):
    return Movie.create(
        title=movie.title
    )


@router.post('/create', response_model=ReviewResponseModel)
async def create_review(user_review: ReviewRequestModel):
    return UserReview.create(
        user=user_review.user,
        movie=user_review.movie,
        review=user_review.review,
        score=user_review.score
    )
