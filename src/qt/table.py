from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt6.QtCore import QSize, Qt
from qt.menu import TableMenu

class Table(QTableWidget):
    def __init__(self, names, row_count, data, num_header, data_base_table):
        QTableWidget.__init__(self)

        self.db_table = data_base_table

        self.setColumnCount(num_header)
        self.setRowCount(row_count)
        self.setHorizontalHeaderLabels(names)

        for row in range(len(data)):
            for c in range(num_header):
                cell = QTableWidgetItem(str(data[row][c]))
                self.setItem(row, c, cell)
        
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.__menu__)

        self.hideColumn(0)

        self.itemChanged.connect(self.__item_changed__)

        self.setMinimumSize(QSize(449, 80))

    def __item_changed__(self, item):

        if (item.column() != 0):
            cell = self.item(item.row(), item.column())
            id = self.item(item.row(), 0)
            self.db_table.cell_changed(int(id.text()), item.column(), cell.text())

    def __menu__(self, pos):
        row = self.row(self.itemAt(pos))

        menu = TableMenu(self)

        menu.set_row2delete(row)

        menu.exec(self.mapToGlobal(pos))
        