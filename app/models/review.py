from . import models, database
from .user import User


class Movie(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        database = database
        table_name = 'movies'

    def __str__(self):
        return self.title


class UserReview(models.Model):
    user = models.ForeignKeyField(
        User,
        db_column='user_id',
        backref='reviews'
    )
    movie = models.ForeignKeyField(
        Movie,
        db_column='movie_id',
        backref='reviews'
    )
    review = models.TextField()
    score = models.IntegerField()

    class Meta:
        database = database
        table_name = 'user_reviews'

    def __str__(self):
        return f'{self.user.username} - {self.movie}'

