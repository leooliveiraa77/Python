from sqlmodel import SQLModel, create_engine, Session, select
from pathlib import Path
from app.models import *

BASE_DIR = Path(__file__).resolve().parent
sqlite_file_name = BASE_DIR / 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=True)

def create_Users(user):

    user_acc = User(user_name=user.user_name, email=user.email, password_hash=user.password_hash, acc_crated_date=user.acc_crated_date)

    with Session(engine) as session:
        session.add(user_acc)    
        session.commit()
        session.refresh(user_acc)
        return user_acc

def select_Users():
    with Session(engine) as session:
        statement = select(User)
        result= session.exec(statement)
        users = result.all()
        # users = session.exec(select(User)).all same effect as previous lines
        print(f'test: {users}')
        return users

def creat_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print('Done!')