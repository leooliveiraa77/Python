from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    user_name: str
    email: str = Field(index=True, unique=True)
    password_hash: str
    acc_crated_date: str | None

