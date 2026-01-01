from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()
users = (17,)

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None

@app.get('/')
def read_root():
    return {'Hello world'}

@app.get('/login/{user_id}')
def read_item(user_id: int, q: str | None = None):
    if not user_id in users:
        raise HTTPException(status_code=404, detail= 'User not found')
    return {'User_id': user_id, 'q': q}

@app.put('/item/{item_id}')
def update_item(item_id: int, item: Item):
    return{'item_price': Item.price, 'item_id': item_id}

