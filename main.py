import uvicorn
from fastapi import FastAPI
from models import database as connection
from utils import list_tables

from routes.user import router as user_router

app = FastAPI(
    title='Reseña de peliculas',
    description='Coloca tus reseñas de tus pelis favoritas',
    version='1.0'
)

app.include_router(user_router)


@app.on_event('startup')
async def startup():
    if connection.is_closed():
        connection.connect(list_tables)


@app.on_event('shutdown')
async def shutdown():
    if not connection.is_closed():
        connection.close()

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='127.0.0.1',
        port=5000
    )
