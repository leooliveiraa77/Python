from sqlmodel import SQLModel,create_engine, Field, Session, select, col
from pathlib import Path

#creating the path for db and the engine
BASE_DIR = Path(__file__).resolve().parent
sqlite_file_name = BASE_DIR / 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=False)

#struturing table
class Task(SQLModel, table=True):
    id: int | None = Field(default= None, primary_key=True)
    task: str
    status: bool

def create_db_and_tables():

    SQLModel.metadata.create_all(engine)
    print('done!')
    return 'Done!'
    
def add_task_db(task, status = False):
    task_user = Task(task= task, status= status)
    with Session(engine) as session:
        session.add(task_user)
        session.commit()

def get_all_task_db():
    with Session(engine) as session:
        tasks = session.exec(select(Task)).all()
        return tasks

def remove_by_id_db(user_id):
    with Session(engine) as session:
        task = session.exec(select(Task).where(col(Task.id ) == user_id)).first()
        if task:
            session.delete(task)
            session.commit()        
            return True
        else:
            return False

def update_status_by_add(user_id):
    with Session(engine) as session:
        task = session.exec(select(Task).where(col(Task.id) == user_id)).first()
        if task:
            task.status = True if task.status == False else False
            session.commit()
            return True
        else:
            return False

def get_task_by_status_db(status):
    with Session(engine) as session:
        task_list = session.exec(select(Task). where(col(Task.status) == status)).all()
        if task_list:
            return task_list
        else:
            return False