from PyQt6.QtWidgets import QMenu

class TableMenu(QMenu):
    def __init__(self, table):
        QMenu.__init__(self)

        self.row = None
        self.table = table

        del_action = self.addAction("Удалить строку")

        # Connect the actions to methods
        del_action.triggered.connect(self.del_action_triggered)

    def set_row2delete(self, row):
        self.row = row

    def del_action_triggered(self):
        if (self.row != None):
            self.table.db_table.delete_row(str(self.table.item(self.row , 0).text()))

            self.table.removeRow(self.row)