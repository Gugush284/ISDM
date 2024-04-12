import sqlite3

class DB():
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

class DB_Table():
    def __init__(self, data_base, names):
        self.db = data_base
        self.header_labels = names
    
    def labels(self):
        return self.header_labels

class DB_Table_equipment(DB_Table):
    def __init__(self, data_base):
        names = [
            "id",
            "Component",
            "Functions",
            "Structure"
        ]

        DB_Table.__init__(self, data_base, names)

        self.db.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS equipment (
            id INTEGER PRIMARY KEY,
            Component Name TEXT,
            Functions TEXT,
            Structure TEXT
            )
            '''
        )

        self.db.connection.commit()
    
    def row_count(self):
        self.db.cursor.execute("select count(*) from equipment")
        row_count = self.db.cursor.fetchone()[0]

        return row_count
    
    def select_all_data(self):
        self.db.cursor.execute("select * from equipment")
        
        return self.db.cursor.fetchall()
    
    def cell_changed(self, id, column, text):
        label = self.header_labels[column]
        
        string = "UPDATE equipment SET " + str(label) + " = \"" + str(text) + "\" WHERE id = " + str(id) + ";"

        self.db.cursor.execute(string)

        self.db.connection.commit()

    def new_row(self):
        string = "INSERT INTO equipment (Functions) VALUES (NULL);"
        
        self.db.cursor.execute(string)

        self.db.connection.commit()

        self.db.cursor.execute("SELECT last_insert_rowid()")

        return self.db.cursor.fetchone()[0]
    
    def get_row(self, id: str):
        string = "select * from equipment WHERE id = " + id + ";"
        self.db.cursor.execute(string)
        
        return self.db.cursor.fetchone()
    
    def delete_row(self, id: str):
        string = "DELETE from equipment WHERE id = " + id + ";"

        self.db.cursor.execute(string)

        self.db.connection.commit()

        


