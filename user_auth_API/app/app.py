from fastapi import FastAPI, HTTPException
from app.schemas import NewUser, NewBook
from app.db import (create_users, select_users, select_user_by_email, update_user_by_email, delete_user_by_mail, select_books, creat_books)

app = FastAPI()

@app.get('/')
def read_root_api():
    return {'Hello world'}

@app.get('/login')
def login_handler_api(email: str):
    user = select_user_by_email(email)

    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    
    return user

@app.get('/user/all')
def get_all_users_api():
    return select_users()


@app.post('/new_user/')
def create_user_api(user: NewUser):
    return create_users(user)
    
@app.put('/users/{user_email}')
def update_item_api(user_email: str, new_user_password: str|None = None,  new_user_name: str | None = None):
    user = select_user_by_email(user_email)

    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    elif user.email == user_email:
       updated_user = update_user_by_email(user_email, new_user_password, new_user_name)
       return updated_user

@app.delete('/user/delete/')
def delete_user_by_mail_api(email: str):
    deleted_user = delete_user_by_mail(email)
    confirmation = select_user_by_email(email)
    
    if not deleted_user:
        raise HTTPException(status_code=404, detail= 'User not found')
    elif not confirmation:
        return {'deleted_user': deleted_user} 

@app.get('/book/all')
def get_all_books_api():
    books = select_books()
    print(books)   
    return books

@app.post('/book/new_book/')
def creat_book_api(book: NewBook):
    return creat_books(book)
        