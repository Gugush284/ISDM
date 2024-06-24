from PyQt6.QtWidgets import QTableWidget
from PyQt6.QtCore import QSize
from PyQt6.QtCore import Qt
from qt.menu import TableMenu

class Table(QTableWidget):
    def __init__(self, names, row_count, column_count, data_base_table):
        QTableWidget.__init__(self)

        self.num_db_header = len(names)

        self.db_table = data_base_table

        self.setColumnCount(column_count)
        self.setRowCount(row_count)
        self.setHorizontalHeaderLabels(names)

        self.setMinimumSize(QSize(449, 80))

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.__menu__)

    def __menu__(self, pos):
        row = self.row(self.itemAt(pos))

        menu = TableMenu(self)

        menu.set_row(row)

        menu.exec(self.mapToGlobal(pos))