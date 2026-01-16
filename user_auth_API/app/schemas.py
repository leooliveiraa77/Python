from pydantic import BaseModel

#test
class NewUser(BaseModel):
    user_name: str
    email: str
    password_hash: str
    acc_crated_date: str | None
    
class NewBook(BaseModel):
    title: str
    author: str
    date: str
    edition: str