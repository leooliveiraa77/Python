from sqlmodel import SQLModel, create_engine, Session, select, col
from pathlib import Path
from app.models import *

BASE_DIR = Path(__file__).resolve().parent
sqlite_file_name = BASE_DIR / 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

connect_args = {'check_same_thread': False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def creat_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print('Done!')

def create_users(user):

    user_acc = User(user_name=user.user_name, email=user.email, password_hash=user.password_hash, acc_crated_date=user.acc_crated_date)

    with Session(engine) as session:
        session.add(user_acc)    
        session.commit()
        session.refresh(user_acc)
        return user_acc

def select_users():
    with Session(engine) as session:
        statement = select(User)
        result= session.exec(statement)
        users = result.all()
        # users = session.exec(select(User)).all same effect as previous lines
        print(f'test: {users}')
        return users
    
def select_user_by_email(email):
    with Session(engine)as session:
        statement = select(User).where(col(User.email) == email)
        result = session.exec(statement).first()
        return result
    
def update_user_by_email(email, new_user_password, new_user_name):
    with Session(engine) as session:
        user = session.exec(select(User).where(col(User.email) == email)).first()
        if new_user_password:
            user.password_hash = new_user_password
        if new_user_name:
            user.user_name = new_user_name
        
        session.add(user)
        session.commit()
        session.refresh(user)

    return user

def delete_user_by_mail(email):
    with Session(engine) as session:
        user = session.exec(select(User).where(col(User.email) == email)).first()
        if user:
            session.delete(user)
            session.commit()
        
        return user

def creat_books(book):
    with Session(engine) as session:
        book = Book(book_title=book.title, book_author= book.author, publish_date= book.date, book_edition= book.edition)
        session.add(book)
        session.commit()
        session.refresh(book)
        return book

def select_books():
    with Session(engine) as session:
        all_books_list = session.exec(select(Book)).all()
        return all_books_list
        
