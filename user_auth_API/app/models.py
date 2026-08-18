from sqlmodel import SQLModel, Field, Relationship
from datetime import date

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_name: str
    email: str = Field(index=True, unique=True)
    password_hash: str
    acc_created_date: date | None
    role: str = "user"
    books_borrowed: list['Book'] = Relationship(back_populates='borrowed_for')

class Book(SQLModel, table=True):
    book_id: int | None = Field(default= None, primary_key=True)
    book_title: str
    book_author: str
    publish_date: str
    book_edition: str
    user_id: int | None = Field(default= None, foreign_key='user.id', index= True)
    borrowed_for: User | None = Relationship(back_populates='books_borrowed')

#criar uma tabela loan (emprestimos), regitrando o histórico de empretimos feitos
