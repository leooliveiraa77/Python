import sqlite3

CREATE_BOOKS_TABLE = "CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, year TEXT)"
INSERT_BOOK = "INSERTE INTO books (title, author, year) VALUES (?, ?, ?)"
SELECT_ALL_BOOKS = 'SELECT * from bookS'

def get_connection():
    return sqlite3.connect('database.db')
    #connection: gerencia transações (commit, rollback, close)
    #cursor: executa queries e lê resultados

def create_tables(connection):
    with connection() as conn:
        cursor = conn.cursor()

        cursor.execute(CREATE_BOOKS_TABLE)

        return cursor.fetchall()
    
def add_book(connection, title, author, year):
    with connection() as conn:
        cursor = conn.cursor()

        cursor.execute(INSERT_BOOK, (title, author, year))


print(create_tables(get_connection))