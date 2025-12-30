import sqlite3
from pathlib import Path

CREATE_BOOKS_TABLE = "CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, year INT, status TEXT)"
INSERT_BOOK = "INSERT INTO books (title, author, year, status) VALUES (?, ?, ?, ?)"
SELECT_ALL_BOOKS = 'SELECT * FROM books'
SELECT_BOOK_BY_STATUS = 'SELECT * FROM books WHERE status = ?'
UPDATE_BOOK_STATUS= 'UPDATE books SET status = ? WHERE id = ?'
DELETE_BOOK_BY_ID = 'DELETE FROM books WHERE id = ?'

def get_connection():
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / 'database.db'

    return sqlite3.connect(file_path)
    #connection: gerencia transações (commit, rollback, close)
    #cursor: executa queries e lê resultados

def create_tables(connection):
    with connection() as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_BOOKS_TABLE)
    
def add_book(connection, title, author, year, status):
    with connection() as conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_BOOK, (title, author, year, status))

def get_all_books(connection):
    with connection() as conn:
        cursor = conn.cursor()
        cursor.execute(SELECT_ALL_BOOKS)
        return cursor.fetchall()

def delete_book(connection, reading_id):
    with connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books WHERE id = ?', (reading_id,))
        book_deleted = cursor.fetchone()
        cursor.execute(DELETE_BOOK_BY_ID, (reading_id))
        return book_deleted
    

def get_books_by_status(connection, status):
    with connection() as conn:
        cursor = conn.cursor()
        cursor.execute(SELECT_BOOK_BY_STATUS, (status,))
        filter = cursor.fetchall()
        return filter
    
def update_status(connection, new_status, id):
    with connection() as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE_BOOK_STATUS, (new_status, id))
        cursor.execute('SELECT * FROM books WHERE id = ?',(id,))
        reading_updated = cursor.fetchone()
        return reading_updated