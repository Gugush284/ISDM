from PyQt6.QtWidgets import QTableWidget
from PyQt6.QtCore import QSize

class Table(QTableWidget):
    def __init__(self, names, row_count, column_count, data_base_table):
        QTableWidget.__init__(self)

        self.db_table = data_base_table

        self.setColumnCount(column_count)
        self.setRowCount(row_count)
        self.setHorizontalHeaderLabels(names)

        self.setMinimumSize(QSize(449, 80))