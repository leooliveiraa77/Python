from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from app.schemas import BookCreate, BookResponse, UserCreate, UserResponse, UserUpdate, Token
from app.db import (get_session, create_users, select_users, select_user_by_email, update_user_by_email, delete_user_by_email, select_books, create_books)
from app.services import authenticate_user
from app.security import create_access_token
from app.auth import get_current_user, require_admin

app = FastAPI()

@app.get('/')
def read_root_api():
    return {'Hello world'}

@app.post('/login/', response_model = Token)
def login_handler_api(*, session : Session = Depends(get_session),form_data: OAuth2PasswordRequestForm = Depends()):

    user = authenticate_user(session, form_data.username, form_data.password)

    if user is None:
        raise HTTPException(status_code=404, detail= 'User not found')

    access_token = create_access_token(data={'sub': user.email})
    return Token(access_token=access_token, token_type= "bearer")


@app.get('/users/', response_model= list[UserResponse])
def get_all_users_api(*, session: Session = Depends(get_session), user = Depends(require_admin)):
    return select_users(session)


@app.post('/new-user/')
def create_user_api(*, session : Session = Depends(get_session), user: UserCreate):
    return create_users(session, user)
    
@app.patch('/users/{user_email}')
def update_item_api(*, session : Session = Depends(get_session), user_email: str, user_update: UserUpdate, user = Depends(get_current_user)):
    target_user = select_user_by_email(session, user_email)

    if not target_user:
            raise HTTPException(status_code=404, detail='User not found')
    
    if user.email != target_user.email:
        raise HTTPException(status_code= 403, detail= "You don't have permission to update this user")

    updated_user = update_user_by_email(session, user_email, user_update.new_user_password, user_update.new_user_name)
    return updated_user

@app.delete('/users/{user_email}')
def delete_user_by_email_api(*, session : Session = Depends(get_session),user_email: str, user = Depends(get_current_user)):

    if user.email != user_email:
        raise HTTPException(status_code=403, detail= "You don't have permission to delete this user")

    deleted_user = delete_user_by_email(session, user_email)
    confirmation = select_user_by_email(session, user_email)
    
    if not deleted_user:
        raise HTTPException(status_code=404, detail= 'User not found')
    elif not confirmation:
        return {'deleted_user': deleted_user} 

@app.get('/books/', response_model=list[BookResponse])
def get_all_books_api(*, session : Session = Depends(get_session), user = Depends(get_current_user)):
    books = select_books(session)
    print(books)   
    return books

@app.post('/new-book/', response_model= BookResponse)
def creat_book_api(*, session:Session = Depends(get_session),book: BookCreate, user = Depends(require_admin)):
    return create_books(session, book)
        