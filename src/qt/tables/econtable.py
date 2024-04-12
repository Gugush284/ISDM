from qt.tables.table import Table
from db.DbCore import DB_Table_econ

class ECTable(Table):
    def __init__(self, tecon: DB_Table_econ):
        Table.__init__(self, tecon.header_labels, tecon.row_count(), len(tecon.header_labels), tecon)

        self.hideColumn(0)