import sqlite3

class DB():
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS equipment (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
            )
            '''
        )

        self.connection.commit()

    def close(self):
        self.connection.close()

class DB_Table():
    def __init__(self, data_base, names):
        self.db = data_base
        self.header_labels = names
    
    def labels(self):
        return self.header_labels

class DB_Table_equipment(DB_Table):
    def __init__(self, data_base, names):
        DB_Table.__init__(self, data_base, names)
    
    def row_count(self):
        self.db.cursor.execute("select count(*) from equipment")
        row_count = self.db.cursor.fetchone()[0]

        return row_count
    
    def select_all_data(self):
        self.db.cursor.execute("select * from equipment")
        
        return self.db.cursor.fetchall()



