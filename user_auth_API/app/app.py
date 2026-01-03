from fastapi import FastAPI, HTTPException
from app.schemas import NewUser
from app.db import create_users, select_users, select_user_by_email, update_user_by_email

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello world'}

@app.get('/login')
def login_handler(email: str):
    user = select_user_by_email(email)

    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    
    return user

@app.get('/users/')
def get_all_users():
    return select_users()


@app.post('/new_user/')
def create_user(user: NewUser):
    return create_users(user)
    
@app.put('/users/{user_email}')
def update_item(user_email: str, new_user_password: str|None = None,  new_user_name: str | None = None):
    user = select_user_by_email(user_email)

    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    elif user.email == user_email:
       updated_user = update_user_by_email(user_email, new_user_password, new_user_name)
       return updated_user
    

    
