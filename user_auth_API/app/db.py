from sqlmodel import SQLModel, create_engine
from pathlib import Path
from . import models

BASE_DIR = Path(__file__).resolve().parent
sqlite_file_name = BASE_DIR / 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=True)

def creat_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print('Done!')