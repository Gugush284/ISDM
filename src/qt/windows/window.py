from PyQt6.QtWidgets import QGridLayout, QWidget, QTableWidgetItem, QPushButton
from PyQt6.QtCore import QSize
from db.DbCore import DB_Table_econ

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

        AddButton = QPushButton("Add row")

        AddButton.clicked.connect(self.__add_row__)

        grid_layout.addWidget(self.table, 0, 0) 

        grid_layout.addWidget(AddButton, 450, 0)

    def __add_row__(self):
        row = self.table.rowCount()
        
        id = self.table.db_table.new_row(
            value=self.callback_component, 
            column = self.callback_component_type
        )

        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem(str(id)))
        self.table.setItem(row, 1, QTableWidgetItem(self.callback_component))
        for column in range(2, len(self.table.db_table.header_labels)):
            self.table.setItem(row, column, QTableWidgetItem("-"))