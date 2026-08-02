from sqlmodel import SQLModel, create_engine, Session, select, col
from pathlib import Path
from app.models import *
from datetime import date
from app.security import password_hash

BASE_DIR = Path(__file__).resolve().parent
sqlite_file_name = BASE_DIR / 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

connect_args = {'check_same_thread': False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print('Done!')

def get_session():
    with Session(engine) as session:
        yield session

def create_users(session : Session, user: User):
    

    user_acc = User(user_name=user.user_name, email=user.email, password_hash=password_hash.hash(user.password_hash), acc_created_date=date.today())

    session.add(user_acc)    
    session.commit()
    session.refresh(user_acc)
    return user_acc

def select_users(session):
        statement = select(User)
        result= session.exec(statement)
        users = result.all()
        # users = session.exec(select(User)).all same effect as previous lines
        print(f'test: {users}')
        return users
    
def select_user_by_email(session: Session, email: str):
    statement = select(User).where(col(User.email) == email)
    result = session.exec(statement).first()
    return result
    
def update_user_by_email(session: Session, email, new_user_password, new_user_name):

    user = session.exec(select(User).where(col(User.email) == email)).first()
    
    if not user:
        return None
    
    if new_user_password:
        user.password_hash = new_user_password
    if new_user_name:
        user.user_name = new_user_name
    
    session.add(user)
    session.commit()
    session.refresh(user)

    return user

def delete_user_by_email(session, email):    
    user = session.exec(select(User).where(col(User.email) == email)).first()
    if user:
        session.delete(user)
        session.commit()
    
    return {'user': user, 'Ok': True}

def create_books(session : Session, book):
    book = Book(book_title=book.book_title, book_author= book.book_author, publish_date= book.publish_date, book_edition= book.book_edition)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def select_books(session : Session):
    all_books_list = session.exec(select(Book)).all()
    return all_books_list
        
