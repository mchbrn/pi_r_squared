import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    db = r"db/sqlite.db"

    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table():
    todo = """CREATE TABLE IF NOT EXISTS todo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date DATE,
                activity VARCHAR(30),
                recurrence VARCHAR(10),
                completed INTEGER(1)
            );"""

    conn = create_connection()

    if conn is not None:
        query(conn, todo)
    else:
        print("Error connecting to database.")

def create_query(sql):
    conn = create_connection()
    
    if conn is not None:
        try:
            query(conn, sql)
        except:
            print("Error couldn't connect barry")

    else:
        print("Query Error")

def get(sql):
    conn = create_connection()

    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except Error as e:
           print(e) 
    else:
        print("Error connecting to database")

def query(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except Error as e:
        print(e)
        print("No access")

if __name__ == "__main__":
    create_table()
