import sqlite3

def connect(name):
    connection = sqlite3.connect(name)
    cursor = connection.cursor()

    return connection, cursor

def create_tables(connection, cursor):
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS equipment (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        '''
    )

    connection.commit()

def close(connection):
    connection.close()