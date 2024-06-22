from db.DbCore import DB_Table

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
    
    def get_pair(self, fc: str):
        string = "select Fcomponent, Scomponent from " + self.table_name + " WHERE Fcomponent = '" + fc + "';"
        self.db.cursor.execute(string)
        
        return self.db.cursor.fetchall()
    
    def delete_Fcomponent(self, component: str):
        string = "DELETE from " + self.table_name + \
            " WHERE Fcomponent = '" + component + \
            "';"

        self.db.cursor.execute(string)

        self.db.connection.commit()

    def delete_Scomponent(self, component: str):
        string = "DELETE from " + self.table_name + \
            " WHERE Scomponent = '" + component + \
            "';"

        self.db.cursor.execute(string)

        self.db.connection.commit()

    