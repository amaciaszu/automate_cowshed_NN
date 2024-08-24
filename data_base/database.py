import sqlite3
import os

def get_db_connection():
    abspath = os.path.abspath(__file__)
    dbpath = os.path.join(os.path.dirname(abspath), 'automated_cowshed.db')
    conn = sqlite3.connect(dbpath)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cows (
        id TEXT PRIMARY KEY,
        name TEXT, 
        birthdate DATE NOT NULL        
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS measurements (
        sensor_id TEXT,
        cow_id TEXT,
        timestamp DATETIME,
        value DOUBLE
        , PRIMARY KEY (sensor_id, cow_id, timestamp)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sensors (
        id TEXT PRIMARY KEY,
        unit TEXT
    )
    ''')

    conn.commit()
    conn.close()