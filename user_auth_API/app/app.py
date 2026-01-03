from fastapi import FastAPI, HTTPException
from app.schemas import NewUser
from app.db import create_Users, select_Users

app = FastAPI()

@app.get('/')
def read_root():
    return {f'Hello world'}

@app.get('/users/')
def get_all_users():
    return select_Users()


@app.post('/new_user/')
def create_user(user: NewUser):
    return create_Users(user)
    
@app.put('/item/{item_id}')
def update_item(item_id: int, item: NewUser):
    return{'item_price': NewUser.name, 'item_id': item_id}
