from fastapi import APIRouter


book_rt = APIRouter()


@book_rt.get("")
def get_books():
    pass


@book_rt.get("")
def get_book():
    pass


@book_rt.post("")
def post_book():
    pass


@book_rt.put("")
def update_book():
    pass


@book_rt.delete("")
def delete_book():
    pass
