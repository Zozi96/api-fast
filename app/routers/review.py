from typing import List
from fastapi import APIRouter, HTTPException

from ..models.user import User
from ..models.review import UserReview, Movie
from ..schemas.review import (
    MovieResponseModel, MovieRequestModel, ReviewRequestModel, ReviewRequestPutModel, ReviewResponseModel
)

router = APIRouter(prefix='/reviews')


@router.post('/movies/create', response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):
    return Movie.create(
        title=movie.title
    )


@router.post('/create', response_model=ReviewResponseModel)
async def create_review(user_review: ReviewRequestModel):
    if User.select().where(User.id == user_review.user).first() is None:
        raise HTTPException(
            status_code=404,
            detail='User not found'
        )

    if Movie.select().where(Movie.id == user_review.movie).first() is None:
        raise HTTPException(
            status_code=404,
            detail='Movie not found'
        )

    return UserReview.create(
        user=user_review.user,
        movie=user_review.movie,
        review=user_review.review,
        score=user_review.score
    )


@router.get('/list', response_model=List[ReviewResponseModel])
async def get_reviews(page: int = 1, limit: int = 10):
    reviews = UserReview.select().paginate(page, limit)
    return [review for review in reviews]


@router.get('/{review_id}', response_model=ReviewResponseModel)
async def get_review(review_id: int):
    user_review = UserReview.select().where(
        UserReview.id == review_id
    ).first()

    if user_review is None:
        raise HTTPException(
            status_code=404,
            detail='Review not found'
        )
    return user_review


@router.put('/{review_id}/edit', response_model=ReviewResponseModel)
async def edit_review(review_id: int, review_request: ReviewRequestPutModel):
    user_review = UserReview.select().where(
        UserReview.id == review_id
    ).first()

    if user_review is None:
        raise HTTPException(
            status_code=404,
            detail='Review not found'
        )

    user_review.review = review_request.review
    user_review.score = review_request.score
    user_review.save()

    return user_review


@router.delete('/{review_id}/delete')
async def delete_review(review_id: int):
    user_review = UserReview.select().where(
        UserReview.id == review_id
    ).first()

    if user_review is None:
        raise HTTPException(
            status_code=404,
            detail='Review not found'
        )
    user_review.delete_instance()
    return user_review
