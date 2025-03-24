from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from routes.book_router import book_rt

app = FastAPI()

app.include_router(book_rt)
