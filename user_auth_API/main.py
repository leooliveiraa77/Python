import uvicorn 
from app.db import creat_db_and_tables, create_users, select_users


def main():
    creat_db_and_tables()
    uvicorn.run(app='app.app:app', host= '127.0.0.1', port=8000)

if __name__ == '__main__':
    main()



