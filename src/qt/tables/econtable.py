from qt.tables.table import Table
from db.connection import DB_Table_econ
from PyQt6.QtWidgets import QTableWidgetItem
from qt.menu import PconMenu

class ECTable(Table):
    def __init__(self, tecon: DB_Table_econ, callback_comp, callback_type):
        self.callback_component = callback_comp
        self.callback_type = callback_type

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

    def add_row(self):
        row = self.rowCount()
        
        id = self.db_table.new_row(
            value= self.callback_component, 
            column = self.callback_type
        )

        self.insertRow(row)

        self.setItem(row, 0, QTableWidgetItem(str(id)))
        self.setItem(row, 1, QTableWidgetItem(self.callback_component))
        for column in range(2, len(self.db_table.header_labels)):
            self.setItem(row, column, QTableWidgetItem(""))

    def __menu__(self, pos):
        row = self.row(self.itemAt(pos))

        menu = PconMenu(self)

        menu.set_row(row)

        menu.exec(self.mapToGlobal(pos))

    def reboot(self):
        print("reboot")

        data = self.db_table.get_connections(self.callback_component)

        print(data)

        self.setRowCount(self.db_table.row_count_where(self.callback_type + " = '" + self.callback_component + "'"))

        for row in range(len(data)):
            for c in range(len(self.db_table.header_labels)):
                cell = QTableWidgetItem(str(data[row][c]))
                self.setItem(row, c, cell)
