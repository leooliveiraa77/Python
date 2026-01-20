from pydantic import BaseModel

#test
class NewUser(BaseModel):
    user_name: str
    email: str
    password_hash: str
    acc_crated_date: str
    
class NewBook(BaseModel):
    book_title: str
    book_author: str
    publish_date: str
    book_edition: str