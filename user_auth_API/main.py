import uvicorn 
from app.db import create_db_and_tables


def main():
    create_db_and_tables()
    uvicorn.run(app='app.app:app', host= '127.0.0.1', port=8000, reload= True)
    
    
if __name__ == '__main__':
    main()



