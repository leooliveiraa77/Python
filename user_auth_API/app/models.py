from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    user_name: str
    email: str = Field(index=True, unique=True)
    password_hash: str
    acc_crated_date: str | None

class Book(SQLModel, table=True):
    book_id: int | None = Field(default= None, primary_key=True)
    book_title: str
    book_author: str
    publish_date: str
    book_edition: str
    borrowed_for: int | None = Field(default= None, foreign_key='user.user_id', index= True)


