import sqlite3

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