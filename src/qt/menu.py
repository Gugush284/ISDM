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

    def set_row(self, row):
        self.row = row

    def del_action_triggered(self):
        if (self.row != None):
            self.table.db_table.delete_row(str(self.table.item(self.row , 0).text()))

            self.table.removeRow(self.row)

    def add_action_triggered(self):
        self.table.add_row()

class PconMenu(TableMenu):
    def __init__(self, table):
        TableMenu.__init__(self, table)

        reverse = self.addAction("Add reversed connection")

        reverse.triggered.connect(self.reverse_action_triggered)

    def __reverse_action_helper__(
        self, 
        fcomponent, 
        scomponent,
        ctype,
        connections_list
    ):
        connections = ", ".join(str(x) for x in connections_list)

        self.table.db_table.new_row(
            "Fcomponent, Scomponent, Connections, Type",
            scomponent + "', '" + fcomponent + "', '" + connections + "', '" + ctype
        )  

    def reverse_action_triggered(self):
        fcomponent = str(self.table.item(self.row , 1).text())
        scomponent = str(self.table.item(self.row , 2).text())

        ctype = str(self.table.item(self.row , 4).text())

        connections_list = list(reversed(self.table.item(self.row , 3).text().split(', ')))

        print(connections_list)
        
        self.__reverse_action_helper__(fcomponent, scomponent, ctype, connections_list)

        for i in range(len(connections_list)):
            for j in range(i + 1, len(connections_list)):
                self.__reverse_action_helper__(connections_list[j], connections_list[i], ctype, connections_list[i + 1 : j])

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

        labels.append("Clear")

        self.setLayout(QGridLayout(self))
        lWidget = QListWidget(self)
        self.layout().addWidget(lWidget)

        lWidget.addItems(labels)

        lWidget.itemClicked.connect(self.onItemClicked)
        self.layout().setContentsMargins(0, 0, 0, 0)

    def onItemClicked(self, item):
        if item.text() != "Clear":
            self.itemSelected = item.text()
            
        self.accept()

    def text(self):
        return self.itemSelected
