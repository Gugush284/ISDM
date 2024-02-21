from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton
import sys

class TableWindow(QMainWindow):
    def __init__(self, names, row_count, data, data_base_table):
        QMainWindow.__init__(self)

        self.db_table = data_base_table
        self.num_header = len(names)
 
        self.setMinimumSize(QSize(480, 80))         # Set sizes 
        self.setWindowTitle("Таблица компонентов")    # Set the window title
        central_widget = QWidget(self)              # Create a central widget
        self.setCentralWidget(central_widget)       # Install the central widget
 
        grid_layout = QGridLayout(self)         # Create QGridLayout
        central_widget.setLayout(grid_layout)   # Set this layout in central widget

        self.table = QTableWidget(self)  # Create a table
        self.__init_table__(names, row_count, data)

        AddButton = self.__init_add_button__()
 
        grid_layout.addWidget(self.table, 0, 0)   # Adding the table to the grid
        grid_layout.addWidget(AddButton, 450, 0)

    def __init_table__(self, names, row_count, data):
        self.table.setColumnCount(self.num_header)
        self.table.setRowCount(row_count)
        self.table.setHorizontalHeaderLabels(names)

        for row in range(len(data)):
            for c in range(self.num_header):
                self.table.setItem(row, c, QTableWidgetItem(str(data[row][c])))

        self.table.itemChanged.connect(self.__item_changed__)

        self.table.setMinimumSize(QSize(449, 80))

    def __init_add_button__(self):
        AddButton = QPushButton("Добавить строку")

        AddButton.clicked.connect(self.__add_row__)

        return AddButton

    def __item_changed__(self, item):
        self.table.resizeColumnsToContents()

        if (item.column() != 0):
            cell = self.table.item(item.row(), item.column())
            id = self.table.item(item.row(), 0)
            self.db_table.cell_changed(int(id.text()), item.column(), cell.text())

    def __add_row__(self):
        row = self.table.rowCount()
        
        id = self.db_table.new_row()

        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem(str(id)))
        for column in range(1, self.num_header):
            self.table.setItem(row, column, QTableWidgetItem("-"))

def QTapp():
    return QApplication(sys.argv)