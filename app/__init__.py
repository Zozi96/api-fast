from fastapi import FastAPI
from .models import database as connection
from .list_models import models

from .routers.user import router as user_router
from .routers.review import router as review_router

app = FastAPI(
    title='Reseña de peliculas',
    description='Coloca tus reseñas de tus pelis favoritas',
    version='1.0'
)


# Routers
app.include_router(user_router)
app.include_router(review_router)


@app.on_event('startup')
async def startup():
    if connection.is_closed():
        connection.connect()
    connection.create_tables(models)


@app.on_event('shutdown')
async def shutdown():
    if not connection.is_closed():
        connection.close()
