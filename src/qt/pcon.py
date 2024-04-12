from PyQt6.QtWidgets import QGridLayout, QWidget
from PyQt6.QtCore import QSize
from qt.tables.econtable import ECTable

class AnotherWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setMinimumSize(QSize(1000, 500))         # Set sizes
 
        self.grid_layout = QGridLayout(self)         # Create QGridLayout
        self.setLayout(self.grid_layout)   # Set this layout in central widget

class PhysicalConnectionsWindow(AnotherWindow):
    def __init__(self, dbtable):
        AnotherWindow.__init__(self)

        self.setWindowTitle("Physical Connections Window")    # Set the window title

        self.table = ECTable(dbtable)  # Create a equipment table

        self.grid_layout.addWidget(self.table, 0, 0)   # Adding the table to the grid