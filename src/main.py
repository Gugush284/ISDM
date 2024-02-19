import data
import qt

def main():
    data_base = data.DB('database.db')

    app = qt.QTapp()

    teq = data.DB_Table_equipment(data_base, ["id", "name"])

    window = qt.TableWindow(teq.header_labels, teq.row_count(), teq.select_all_data())
    window.show()

    app.exec()

    data_base.close()

main()