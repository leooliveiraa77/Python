from db import create_db_and_tables
from cli import initApp

if __name__ == '__main__':
    create_db_and_tables()
    initApp()