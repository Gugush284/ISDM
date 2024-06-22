from PyQt6.QtWidgets import QTableWidgetItem, QPushButton
from functools import partial
from db.equipment import DB_Table_equipment
from db.connection import DB_Table_econ
from qt.windows.pcon import PhysicalConnectionsWindow
from qt.tables.table import Table
from qt.menu import MainTableMenu

class ETable(Table):
    def __init__(self, interNames, teq: DB_Table_equipment, tecon: DB_Table_econ):
        Table.__init__(
            self, 
            teq.header_labels + interNames, 
            teq.row_count(), 
            len(teq.header_labels) + len(interNames), 
            teq
        )

        self.num_db_header = len(teq.header_labels)
        data = teq.select_all_data()
        self.table_connections = tecon

        for row in range(len(data)):
            for c in range(len(teq.header_labels)):
                cell = QTableWidgetItem(str(data[row][c]))
                self.setItem(row, c, cell)

            self.add_pcb(row, self.num_db_header)

            self.add_lcb(row, self.num_db_header + 1)

        self.hideColumn(0)

        self.itemChanged.connect(self.__item_changed__)

    def __spc__(self, item):
        self.pcw = PhysicalConnectionsWindow(self.db_table, self.table_connections, item.text())
        self.pcw.show()

    def __slc__(self, row):
        print(self.item(row, 0).text())

    def add_pcb(self,row: int, column: int):
        pButton = QPushButton("Show physical connections")
        pButton.clicked.connect(partial(self.__spc__, self.item(row, 0)))
        self.setCellWidget(row, column, pButton)

    def add_lcb(self,row: int, column: int):
        lButton = QPushButton("Show logical connections")
        lButton.clicked.connect(partial(self.__slc__, row))
        self.setCellWidget(row, column, lButton)

    def __item_changed__(self, item):
        if ((item.column() > 0) and (item.column() < self.num_db_header)):
            id = self.item(item.row(), 0)
            self.db_table.cell_changed(int(id.text()), item.column(), item.text())

    def add_row(self):
        row = self.rowCount()
        
        id = self.db_table.new_row()

        self.insertRow(row)

        self.setItem(row, 0, QTableWidgetItem(str(id)))
        for column in range(1, self.num_db_header):
            self.setItem(row, column, QTableWidgetItem("-"))

        self.add_pcb(row, self.num_db_header)
        self.add_lcb(row, self.num_db_header + 1)

    def __menu__(self, pos):
        row = self.row(self.itemAt(pos))

        menu = MainTableMenu(self, self.table_connections)

        menu.set_row2delete(row)

        menu.exec(self.mapToGlobal(pos))