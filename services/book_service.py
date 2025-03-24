from db.database import database
from bson import ObjectId
from models.models import Book
from fastapi.responses import JSONResponse
from fastapi import status


def create_book_s(book: Book):
    collection = database.get_collection("books")
    book_dict = book.dict()
    r = collection.insert_one(book_dict)
    return JSONResponse(
        content={"id": str(r.inserted_id), "content": str(book_dict)},
        status_code=status.HTTP_201_CREATED,
    )


def get_book_s(id: str):
    collection = database.get_collection("books")
    try:
        ob_id = ObjectId(id)
    except:
        return JSONResponse(
            content={"message": "book not found"}, status_code=status.HTTP_404_NOT_FOUND
        )

    book = collection.find_one({"_id": ob_id})

    if book:
        return Book(title=book["title"], author=book["author"], genre=book["genre"])
    return None


def get_books_s():
    collection = database.get_collection("books")
    books = list(collection.find({}, {"_id": 0}))
    return books


def update_book_s(id: str, book: Book):
    collection = database.get_collection("books")
    updated_data = {}

    book_dict = book.dict()

    for k, v in book_dict.items():
        if v is not None:
            updated_data[k] = v

    if not updated_data:
        return JSONResponse(
            content={"message": "no data to update"}, status_code=status.HTTP_200_OK
        )

    try:
        res = collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
    except Exception as e:
        return JSONResponse(
            content={"message": "book not found"}, status_code=status.HTTP_404_NOT_FOUND
        )

    return JSONResponse(
        content={"message": "book updated", "content": str(updated_data)},
        status_code=status.HTTP_201_CREATED,
    )


def delete_book_s(id: str):
    collection = database.get_collection("books")
    book = get_book_s(id)

    try:
        res = collection.delete_one({"_id": ObjectId(id)})
    except Exception:
        return JSONResponse(
            content={"message": "book not found"},
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return JSONResponse(content={"deleted": str(book)}, status_code=status.HTTP_200_OK)
