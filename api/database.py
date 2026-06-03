import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("documents.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        page_count INTEGER,
        file_size INTEGER,
        upload_date TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_document(filename, page_count, file_size):
    conn = sqlite3.connect("documents.db")
    cursor = conn.cursor()

    cursor.execute("""
                   INSERT INTO documents (filename, page_count, 
                                        file_size, upload_date)
                     VALUES (?, ?, ?, ?)""", 
                    (filename, page_count, file_size, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_all_documents():

    conn = sqlite3.connect("documents.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM documents
    """)

    documents = cursor.fetchall()
    conn.close()
    return documents

def search_documents(search_term):
    conn = sqlite3.connect("documents.db")
    cursor = conn.cursor()
    cursor.execute(""" SELECT *
                   FROM documents
                   WHERE filename LIKE ?
                   """, (f"%{search_term}%",))

    documents = cursor.fetchall()
    conn.close()
    return documents
