from db.DbCore import DB
from db.equipment import DB_Table_equipment
from db.connection import DB_Table_econ
from qt.QtCore import QTapp, MainWindow

def main():
    data_base = DB('database.db')

    app = QTapp()

    teq = DB_Table_equipment(data_base)
    tecon = DB_Table_econ(data_base)

    interNames = ["Physical communication lines" ,"Logical communication lines"]

    window = MainWindow(interNames, teq, tecon)
    window.show()

    app.exec()

    data_base.close()

main()