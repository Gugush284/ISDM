from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
import sys

class TableWindow(QMainWindow):
    def __init__(self, names, row_count, data):
        QMainWindow.__init__(self)
 
        self.setMinimumSize(QSize(480, 80))         # Set sizes 
        self.setWindowTitle("Таблица компонентов")    # Set the window title
        central_widget = QWidget(self)              # Create a central widget
        self.setCentralWidget(central_widget)       # Install the central widget
 
        grid_layout = QGridLayout(self)         # Create QGridLayout
        central_widget.setLayout(grid_layout)   # Set this layout in central widget
 
        table = QTableWidget(self)  # Create a table
        table.setColumnCount(len(names))     #Set three columns
        table.setRowCount(row_count)        # and one row
 
        # Set the table headers
        table.setHorizontalHeaderLabels(names)
 
        # Fill the first line
        for row in range(len(data)):
            table.setItem(row, 0, QTableWidgetItem(str(data[row][0])))
            table.setItem(row, 1, QTableWidgetItem(str(data[row][1])))
 
        # Do the resize of the columns by content
        table.resizeColumnsToContents()
 
        grid_layout.addWidget(table, 0, 0)   # Adding the table to the grid

def QTapp():
    return QApplication(sys.argv)