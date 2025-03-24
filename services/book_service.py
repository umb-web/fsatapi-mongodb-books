from db.database import database
from bson import ObjectId
from models.models import Book
from fastapi.encoders import jsonable_encoder


def create_book_s(book: Book):
    collection = database.get_collection("books")
    book_dict = book.dict()
    r = collection.insert_one(book_dict)
    return {"id": str(r.inserted_id), "content": str(book_dict)}


def get_book_s(id: str):
    collection = database.get_collection("books")
    try:
        ob_id = ObjectId(id)
    except:
        return None

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
        return {"message": "no data to update"}

    res = collection.update_one({"_id": ObjectId(id)}, {"$set": updated_data})

    if res.matched_count == 0:
        return {"message": "book not found"}

    return {"message": "book updated", "content": str(updated_data)}


def delete_book_s(id: str):
    collection = database.get_collection("books")
    book = get_book_s(id)

    try:
        res = collection.delete_one({"_id": ObjectId(id)})
        if res.deleted_count == 0:
            return {"message": "book not found"}
    except Exception as e:
        return {"message": f"error {str(e)}"}
    return {
        "deleted": str(book),
    }
