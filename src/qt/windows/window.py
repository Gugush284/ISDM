from PyQt6.QtWidgets import QGridLayout, QWidget
from PyQt6.QtCore import QSize
from graph.graphCore import Gcore

class AnotherWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setMinimumSize(QSize(1000, 500))        

class ConnectionsWindow(AnotherWindow):
    def __init__(self, table, callback_component="NULL", callback_component_type="NULL"):
        AnotherWindow.__init__(self)

        self.table = table
        self.callback_component = callback_component
        self.callback_component_type = callback_component_type

        self.grid_layout = QGridLayout(self)       
        self.setLayout(self.grid_layout)   

        self.grid_layout.addWidget(self.table, 0, 0)

    def __add_row__(self):
        self.table.add_row()

    def graph(self):
        g = Gcore()

        g.info()
