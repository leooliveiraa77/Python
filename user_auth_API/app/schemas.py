from pydantic import BaseModel

#test
class NewUser(BaseModel):
    name: str
    password: str
    id: int