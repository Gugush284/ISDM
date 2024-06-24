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
        self.table_name = "None"
    
    def labels(self):
        return self.header_labels
    
    def get_row(self, id: str):
        string = "select * from " + self.table_name + " WHERE id = " + id + ";"
        self.db.cursor.execute(string)
        
        return self.db.cursor.fetchone()
    
    def delete_row(self, id: str):
        string = "DELETE from " + self.table_name + " WHERE id = " + id + ";"

        self.db.cursor.execute(string)

        self.db.connection.commit()

    def row_count(self, where = ""):
        self.db.cursor.execute("select count(*) from " + self.table_name + where + ";")

        return self.db.cursor.fetchone()[0]
    
    def row_count_where(self, where: str):

        return self.row_count(where = " WHERE " + where + " ")
    
    def get_comp(self):
        self.db.cursor.execute("select id, Component from " + self.table_name + ";")
        
        return self.db.cursor.fetchall()
    
    def select_all_data(self):
        self.db.cursor.execute("select * from " + self.table_name + ";")
        
        return self.db.cursor.fetchall()
    
    def __new_row__(self, insert: str, select: str):
        print(insert)
        self.db.cursor.execute(insert)

        self.db.connection.commit()

        self.db.cursor.execute(select)

        return self.db.cursor.fetchone()[0]
