from fastapi import FastAPI, HTTPException
from app.schemas import NewUser



app = FastAPI()
users = (17,)



@app.get('/')
def read_root():
    return {f'Hello world'}

@app.get('/login/{user_id}')
def read_item(user_id: int, q: str | None = None):
    if not user_id in users:
        raise HTTPException(status_code=404, detail= 'User not found')
    return {'User_id': user_id, 'q': q}

@app.put('/item/{item_id}')
def update_item(item_id: int, item: NewUser):
    return{'item_price': NewUser.name, 'item_id': item_id}

@app.post('/new_user')
def create_user(user: NewUser) -> NewUser:
    print(f'User {user.name}')
    return NewUser(name= 'farelo', password= 'aboba', id= 123)
