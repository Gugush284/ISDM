from db.DbCore import DB_Table

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