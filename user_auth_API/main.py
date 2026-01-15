import uvicorn 
from app.db import creat_db_and_tables, creat_books, select_books


def main():
    creat_db_and_tables()
    uvicorn.run(app='app.app:app', host= '127.0.0.1', port=8000, reload= True)

if __name__ == '__main__':
    main()



