from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_name: str
    email: str = Field(index=True, unique=True)
    password_hash: str
    acc_crated_date: str | None
    books_borrowed: list['Book'] = Relationship(back_populates='borrowed_for')

class Book(SQLModel, table=True):
    book_id: int | None = Field(default= None, primary_key=True)
    book_title: str
    book_author: str
    publish_date: str
    book_edition: str
    user_id: int | None = Field(default= None, foreign_key='user.id', index= True)
    borrowed_for: User | None = Relationship(back_populates='books_borrowed')


