from fastapi import FastAPI
from routes.book_router import book_rt

app = FastAPI()

app.include_router(book_rt)
