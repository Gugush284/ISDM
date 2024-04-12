from db.DbCore import DB, DB_Table_equipment
from qt.QtCore import QTapp, MainWindow

def main():
    data_base = DB('database.db')

    app = QTapp()

    teq = DB_Table_equipment(data_base)

    interNames = ["Physical communication lines" ,"Logical communication lines"]

    window = MainWindow(interNames, teq.header_labels, teq.row_count(), teq.select_all_data(), teq)
    window.show()

    app.exec()

    data_base.close()

main()