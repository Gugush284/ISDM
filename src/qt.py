from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
import sys

class TableWindow(QMainWindow):
    def __init__(self, names, row_count, data, data_base_table):
        QMainWindow.__init__(self)

        self.db_table = data_base_table
 
        self.setMinimumSize(QSize(480, 80))         # Set sizes 
        self.setWindowTitle("Таблица компонентов")    # Set the window title
        central_widget = QWidget(self)              # Create a central widget
        self.setCentralWidget(central_widget)       # Install the central widget
 
        grid_layout = QGridLayout(self)         # Create QGridLayout
        central_widget.setLayout(grid_layout)   # Set this layout in central widget
 
        self.table = QTableWidget(self)  # Create a table
        self.table.setColumnCount(len(names))
        self.table.setRowCount(row_count)
 
        # Set the table headers
        self.table.setHorizontalHeaderLabels(names)
 
        # Fill the first line
        for row in range(len(data)):
            self.table.setItem(row, 0, QTableWidgetItem(str(data[row][0])))
            self.table.setItem(row, 1, QTableWidgetItem(str(data[row][1])))

        self.table.itemChanged.connect(self.item_changed)
 
        # Do the resize of the columns by content
        self.table.resizeColumnsToContents()
 
        grid_layout.addWidget(self.table, 0, 0)   # Adding the table to the grid

    def item_changed(self, item):
        self.table.resizeColumnsToContents()

        cell = self.table.item(item.row(), item.column())
        id = self.table.item(item.row(), 0)
        self.db_table.cell_changed(int(id.text()), item.column(), cell.text())

def QTapp():
    return QApplication(sys.argv)