from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session
from app.schemas import NewUser, NewBook
from app.db import (get_session, create_users, select_users, select_user_by_email, update_user_by_email, delete_user_by_email, select_books, create_books)

app = FastAPI()

@app.get('/')
def read_root_api():
    return {'Hello world'}

@app.post('/login/')
def login_handler_api(*, session : Session = Depends(get_session),email: str):
    user = select_user_by_email(session, email)

    if not user:
        raise HTTPException(status_code=404, detail='User not found')    
    return user

@app.get('/user/all/', response_model= list[NewUser])
def get_all_users_api(*, session: Session = Depends(get_session)):
    return select_users(session)


@app.post('/new_user/')
def create_user_api(*, session : Session = Depends(get_session), user: NewUser):
    return create_users(session, user)
    
@app.patch('/users/{user_email}')
def update_item_api(*, session : Session = Depends(get_session), user_email: str, new_user_password: str|None = None,  new_user_name: str | None = None):
    user = select_user_by_email(session, user_email)

    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    elif user.email == user_email:
       updated_user = update_user_by_email(session, user_email, new_user_password, new_user_name)
       return updated_user

@app.delete('/user/delete/')
def delete_user_by_mail_api(*, session : Session = Depends(get_session),email: str):
    deleted_user = delete_user_by_email(session, email)
    confirmation = select_user_by_email(session, email)
    
    if not deleted_user:
        raise HTTPException(status_code=404, detail= 'User not found')
    elif not confirmation:
        return {'deleted_user': deleted_user} 

@app.get('/book/all/', response_model=list[NewBook])
def get_all_books_api(*, session : Session = Depends(get_session)):
    books = select_books(session)
    print(books)   
    return books

@app.post('/book/new_book/')
def creat_book_api(*, session:Session = Depends(get_session),book: NewBook):
    return create_books(session, book)
        