from fastapi import APIRouter


book_rt = APIRouter()


@book_rt.get("/books/{id}")
def get_books():
    pass


@book_rt.get("/books")
def get_book():
    pass


@book_rt.post("/books")
def post_book():
    pass


@book_rt.put("/books/{id}")
def update_book():
    pass


@book_rt.delete("/books/{id}")
def delete_book():
    pass
