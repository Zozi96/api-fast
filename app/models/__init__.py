import peewee as db

database = db.MySQLDatabase(
    'api',
    user='root',
    password='admin',
    host='127.0.0.1',
    port=3306
)

models = db
