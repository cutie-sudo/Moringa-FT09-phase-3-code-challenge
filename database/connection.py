import sqlite3

DATABASE_NAME = './database/magazine.db'

def get_db_connection():
    try:
        # Open a connection to the database
        conn = sqlite3.connect(DATABASE_NAME)
        
        # Enable foreign key support (this is important for foreign key constraints)
        conn.execute('PRAGMA foreign_keys = ON')
        
        # Enable row factory to return rows as dictionaries (access by column name)
        conn.row_factory = sqlite3.Row
        
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None