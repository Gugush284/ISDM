from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidgetItem, QPushButton, QHeaderView
from db.DbCore import DB_Table_equipment, DB_Table_econ
import sys
from qt.tables.etable import ETable

class MainWindow(QMainWindow):
    def __init__(self, interNames, teq: DB_Table_equipment, tecon: DB_Table_econ):
        QMainWindow.__init__(self)

        self.num_db_header = len(teq.header_labels)
        self.num_inter_header = len(interNames)
 
        self.setMinimumSize(QSize(1000, 500))         # Set sizes 
        self.setWindowTitle("The table of components")    # Set the window title
        central_widget = QWidget(self)              # Create a central widget
        self.setCentralWidget(central_widget)       # Install the central widget
 
        grid_layout = QGridLayout(self)         # Create QGridLayout
        central_widget.setLayout(grid_layout)   # Set this layout in central widget

        self.table = ETable(interNames, teq, tecon)  # Create a equipment table

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
        for column in range(1, self.num_db_header):
            self.table.setItem(row, column, QTableWidgetItem("-"))

        self.table.add_pcb(row, self.num_db_header)
        self.table.add_lcb(row, self.num_db_header + 1)

    

def QTapp():
    return QApplication(sys.argv)
