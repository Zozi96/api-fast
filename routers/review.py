from fastapi import APIRouter
from models.review import UserReview, Movie
from schemas.review import (
    MovieResponseModel, MovieRequestModel, ReviewRequestModel, ReviewResponseModel
)

router = APIRouter(prefix='/reviews')


@router.post('/movies/create', response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):
    new_movie = Movie.create(
        title=movie.title
    )
    return new_movie


@router.post('/create', response_model=ReviewResponseModel)
async def create_review(user_review: ReviewRequestModel):
    review = UserReview.create(
        user=user_review.user,
        movie=user_review.movie,
        review=user_review.review,
        score=user_review.score
    )

    return review
