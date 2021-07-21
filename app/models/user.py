import hashlib
from . import models, database


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    class Meta:
        database = database
        table_name = 'users'

    def __str__(self):
        return self.username

    @classmethod
    def create_password(cls, password):
        h = hashlib.md5()
        h.update(
            password.encode('utf-8')
        )
        return h.hexdigest()
