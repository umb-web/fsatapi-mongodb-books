from pydantic import BaseModel
from typing import Optional


class Book(BaseModel):
    title: str
    author: str
    year: Optional[str] = None
    genre: str
    pages: Optional[str] = None
