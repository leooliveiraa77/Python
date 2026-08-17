from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    user_name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    user_name: str
    email: str
    acc_created_date: date | None

class UserUpdate(BaseModel):
    new_user_name: str | None = None
    new_user_password: str | None = None

class BookCreate(BaseModel):
    book_title: str
    book_author: str
    publish_date: str
    book_edition: str

class BookResponse(BaseModel):
    book_id: int
    book_title: str
    book_author: str
    publish_date: str
    book_edition: str

class Token(BaseModel):
    access_token: str
    token_type: str
