from sqlmodel import SQLModel,create_engine, Field, Session, select
from pathlib import Path

#creating the path for db and engine
BASE_DIR = Path(__file__).resolve().parent
sqlite_file_name = BASE_DIR / 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=True)

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
        print(tasks)