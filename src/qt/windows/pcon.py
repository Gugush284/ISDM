from qt.tables.econtable import ECTable
from qt.windows.window import ConnectionsWindow
from graph.pgraph import PGraph
from PyQt6.QtWidgets import QPushButton
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

        AddButtonShow = QPushButton("Show")

        AddButtonShow.clicked.connect(self.__graph__)

        self.grid_layout.addWidget(self.table, 0, 0) 

        self.grid_layout.addWidget(AddButtonShow, 500, 0)


    def __get_comp_from_db__(self):
        db_array = self.comptable.get_comp()

        dict = {}

        for elem in db_array:
            dict[elem[1]] = elem[0]
        
        return dict

    def onClicked(self, index):
        row = index.row()
        column = index.column()

        if column == 2 or column == 3:
            components = self.__get_comp_from_db__()

            p = PopUp(list(components.keys()))

            if column == 2:
                if p.exec() == 1:
                    t_item = QTableWidgetItem(p.text())
                    self.table.setItem(row, column, t_item)
            elif column == 3:
                if p.exec() == 1:
                    item = self.table.item(row, column)

                    if item.text() != "" and item.text() != "-" and p.text() != "":
                        connections_list = item.text().split(", ")

                        for i in range(len(connections_list)):
                            connections = ", ".join(str(x) for x in connections_list[i + 1: len(connections_list)])

                            self.table.db_table.new_row(
                                "Fcomponent, Scomponent, Connections, Type",
                                connections_list[i] + "', '" + p.text() + "', '" + connections + "', '" + self.table.item(row, 4).text()
                            )

                        self.table.db_table.new_row(
                            "Fcomponent, Scomponent, Connections, Type",
                            self.table.item(row, 1).text() + "', '" + p.text() + "', '" + "', '" + self.table.item(row, 4).text()
                        )

                        item.setText(item.text() + ", " + p.text())

                    else:
                        if p.text() != "":
                            self.table.db_table.new_row(
                                "Fcomponent, Scomponent, Connections, Type",
                                self.table.item(row, 1).text() + "', '" + p.text() + "', '" + "', '" + self.table.item(row, 4).text()
                            )

                        item.setText(p.text())

                self.grid_layout.removeWidget(self.table)

                self.table.reboot()

                self.grid_layout.addWidget(self.table, 0, 0)

    def __get_callback_comp__(self, dbtable: DB_Table_econ, id):
        return dbtable.get_row(id)[1]
    
    def __graph__(self):
        PGraph(self.table.db_table.get_connections(self.table.callback_component)).graph()