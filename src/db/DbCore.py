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
        self.db.cursor.execute("select Component from " + self.table_name + ";")
        
        return self.db.cursor.fetchall()
    
    def select_all_data(self):
        self.db.cursor.execute("select * from " + self.table_name + ";")
        
        return self.db.cursor.fetchall()
    
    def __new_row__(self, insert: str, select: str):
        self.db.cursor.execute(insert)

        self.db.connection.commit()

        self.db.cursor.execute(select)

        return self.db.cursor.fetchone()[0]

class DB_Table_equipment(DB_Table):
    def __init__(self, data_base):
        names = [
            "id",
            "Component",
            "Functions",
            "Structure"
        ]

        DB_Table.__init__(self, data_base, names)

        self.table_name = "equipment"

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
    
    def cell_changed(self, id, column, text):
        label = self.header_labels[column]
        
        string = "UPDATE equipment SET " + str(label) + " = \"" + str(text) + "\" WHERE id = " + str(id) + ";"

        self.db.cursor.execute(string)

        self.db.connection.commit()

    def new_row(self, column="Functions", value="NULL"):
        if value != "NULL":
            value = "'" + value  + "'"

        return self.__new_row__(
            "INSERT INTO equipment (" + column + ") VALUES (" + value + ");",
            "SELECT last_insert_rowid()"
        )

class DB_Table_econ(DB_Table):
    def __init__(self, data_base):
        names = [
            "id",
            "Fcomponent",
            "Scomponent",
            "Connections"
        ]

        DB_Table.__init__(self, data_base, names)

        self.table_name = "econ"

        self.db.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS econ (
            id INTEGER PRIMARY KEY,
            Fcomponent INTEGER,
            Scomponent INTEGER,
            Connections TEXT
            )
            '''
        )

        self.db.connection.commit()

    def new_row(self, column = "Connections", value="NULL"):
        if value != "NULL":
            value = "'" + value  + "'"
        
        return self.__new_row__(
            "INSERT INTO econ (" + column + ") VALUES (" + value + ");",
            "SELECT last_insert_rowid()"
        )
    
    def cell_changed(self, id, column, text):
        label = self.header_labels[column]
        
        string = "UPDATE econ SET " + str(label) + " = \"" + str(text) + "\" WHERE id = " + str(id) + ";"

        self.db.cursor.execute(string)

        self.db.connection.commit()

    def get_connections(self, fc: str):
        string = "select * from " + self.table_name + " WHERE Fcomponent = '" + fc + "';"
        self.db.cursor.execute(string)
        
        return self.db.cursor.fetchall()
