from qt.tables.econtable import ECTable
from qt.windows.window import ConnectionsWindow
from graph.graphCore import Gcore
from PyQt6.QtWidgets import  QTableWidgetItem
from db.equipment import DB_Table_equipment
from db.connection import DB_Table_econ
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
    
    def __get_connections(self):
        connections = self.table.db_table.get_connections(self.table.callback_component)

        return [(elem[1], elem[2], elem[3]) for elem in connections]
    
    def __graph__(self):
        g = Gcore()
        connections = self.__get_connections()

        g.add_nodes_from_connections(connections)

        g.add_edges_with_label(connections)

        #g.info()

        g.show()