from qt.tables.table import Table
from db.DbCore import DB_Table_econ
from PyQt6.QtWidgets import QTableWidgetItem

class ECTable(Table):
    def __init__(self, tecon: DB_Table_econ, callback_comp, callback_type):
        Table.__init__(self,
            tecon.header_labels,
            tecon.row_count_where(callback_type + " = '" + callback_comp + "'"), 
            len(tecon.header_labels), 
            tecon
        )

        data = tecon.get_connections(callback_comp)

        for row in range(len(data)):
            for c in range(len(tecon.header_labels)):
                cell = QTableWidgetItem(str(data[row][c]))
                self.setItem(row, c, cell)

        self.hideColumn(0)

        self.itemChanged.connect(self.__item_changed__)

    def __item_changed__(self, item):
        if ((item.column() > 1) and (item.column() < self.num_db_header)):
            id = self.item(item.row(), 0)
            self.db_table.cell_changed(int(id.text()), item.column(), item.text())
