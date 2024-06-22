from PyQt6.QtWidgets import QMenu
from PyQt6.QtWidgets import QDialog, QListWidget, QGridLayout

class TableMenu(QMenu):
    def __init__(self, table):
        QMenu.__init__(self)

        self.row = None
        self.table = table

        del_action = self.addAction("Delete row")
        add_action = self.addAction("Add row")

        # Connect the actions to methods
        del_action.triggered.connect(self.del_action_triggered)
        add_action.triggered.connect(self.add_action_triggered)

    def set_row2delete(self, row):
        self.row = row

    def del_action_triggered(self):
        if (self.row != None):
            self.table.db_table.delete_row(str(self.table.item(self.row , 0).text()))

            self.table.removeRow(self.row)

    def add_action_triggered(self):
        print("de")
        self.table.add_row()

class MainTableMenu(TableMenu):
    def __init__(self, table, table_connections):
        TableMenu.__init__(self, table)

        self.table_connections = table_connections

    def del_action_triggered(self):
        if (self.row != None):
            self.table.db_table.delete_row(str(self.table.item(self.row , 0).text()))

            self.table_connections.delete_Fcomponent(self.table.item(self.row , 1).text())
            self.table_connections.delete_Scomponent(self.table.item(self.row , 1).text())

            self.table.removeRow(self.row)

class PopUp(QDialog):
    def __init__(self, labels):
        QDialog.__init__(self)
        self.itemSelected = ""
        self.setLayout(QGridLayout(self))
        lWidget = QListWidget(self)
        self.layout().addWidget(lWidget)
        lWidget.addItems(labels)
        lWidget.itemClicked.connect(self.onItemClicked)
        self.layout().setContentsMargins(0, 0, 0, 0)

    def onItemClicked(self, item):
        self.itemSelected = item.text()
        self.accept()

    def text(self):
        return self.itemSelected
