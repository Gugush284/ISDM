from PyQt6.QtWidgets import QGridLayout, QWidget, QTableWidgetItem, QPushButton
from PyQt6.QtCore import QSize

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

        grid_layout = QGridLayout(self)       
        self.setLayout(grid_layout)   

        AddButtonShow = QPushButton("Show")

        AddButtonShow.clicked.connect(self.__graph__)

        grid_layout.addWidget(self.table, 0, 0) 

        grid_layout.addWidget(AddButtonShow, 500, 0)

    def __add_row__(self):
        self.table.add_row()

    def __graph__(self):
        return