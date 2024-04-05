from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidgetItem, QPushButton, QHeaderView
import sys
from qt.table import Table

class MainWindow(QMainWindow):
    def __init__(self, names, row_count, data, data_base_table):
        QMainWindow.__init__(self)

        self.num_header = len(names)
 
        self.setMinimumSize(QSize(480, 80))         # Set sizes 
        self.setWindowTitle("Таблица компонентов")    # Set the window title
        central_widget = QWidget(self)              # Create a central widget
        self.setCentralWidget(central_widget)       # Install the central widget
 
        grid_layout = QGridLayout(self)         # Create QGridLayout
        central_widget.setLayout(grid_layout)   # Set this layout in central widget

        self.table = Table(names, row_count, data, self.num_header, data_base_table)  # Create a table

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        AddButton = self.__init_add_button__()
 
        grid_layout.addWidget(self.table, 0, 0)   # Adding the table to the grid
        grid_layout.addWidget(AddButton, 450, 0)

    def __init_add_button__(self):
        AddButton = QPushButton("Add row")

        AddButton.clicked.connect(self.__add_row__)

        return AddButton

    def __add_row__(self):
        row = self.table.rowCount()
        
        id = self.table.db_table.new_row()

        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem(str(id)))
        for column in range(1, self.num_header):
            self.table.setItem(row, column, QTableWidgetItem("-"))

    

def QTapp():
    return QApplication(sys.argv)
