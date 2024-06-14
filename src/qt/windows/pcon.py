from qt.tables.econtable import ECTable
from qt.windows.window import ConnectionsWindow
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import  QTableWidgetItem
from db.DbCore import DB_Table_equipment, DB_Table_econ
from qt.menu import PopUp

class PhysicalConnectionsWindow(ConnectionsWindow):
    def __init__(self, comptable: DB_Table_equipment, dbtable: DB_Table_econ, callback_id: int):
        callback_comp = self.__get_callback_comp__(comptable, callback_id)
        callback_comp_type = "Fcomponent"

        table = ECTable(dbtable, callback_comp, callback_comp_type)

        ConnectionsWindow.__init__(
            self, 
            table,
            callback_component= callback_comp,
            callback_component_type = callback_comp_type
        )

        self.comptable = comptable

        self.table.clicked.connect(self.onClicked)

        self.setWindowTitle("Physical Connections Window")    # Set the window title

    def __get_comp_from_db__(self):
        array = []
        db_array = self.comptable.get_comp()

        for a in db_array:
            for elem in a:
                array.append(elem)
        
        return array

    def onClicked(self, index):
        row = index.row()
        column = index.column()

        if column != 2:
            return

        x = self.table.columnViewportPosition(column)
        y = self.table.rowViewportPosition(row) + self.table.rowHeight(row)

        p = PopUp(self.__get_comp_from_db__())
        
        if p.exec() == 1:
            t_item = QTableWidgetItem(p.text())
            self.table.setItem(row, column, t_item)

    def __get_callback_comp__(self, dbtable: DB_Table_econ, id):
        return dbtable.get_row(id)[1]