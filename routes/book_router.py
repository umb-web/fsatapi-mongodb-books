from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.book_service import (
    get_book_s,
    get_books_s,
    delete_book_s,
    update_book_s,
    create_book_s,
)
from models.models import Book

book_rt = APIRouter()


@book_rt.get("/books")
def get_books():
    books = get_books_s()
    return books


@book_rt.get("/books/{id}")
def get_book(id: str):
    book = get_book_s(id)
    return book


@book_rt.post("/books")
def post_book(book: Book):
    res = create_book_s(book)
    return res


@book_rt.put("/books/{id}")
def update_book(id: str, book: Book):
    res = update_book_s(id, book)
    return res


@book_rt.delete("/books/{id}")
def delete_book(id: str):
    res = delete_book_s(id)
    return res
