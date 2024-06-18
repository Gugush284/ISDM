from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidgetItem, QPushButton, QHeaderView
from db.equipment import DB_Table_equipment
from db.connection import DB_Table_econ
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
 
        grid_layout.addWidget(self.table, 0, 0)   # Adding the table to the grid

    def __add_row__(self):
        self.table.add_row()

    

def QTapp():
    return QApplication(sys.argv)
