import data
import qt

def main():
    connection, cursor = data.connect('database.db')

    data.create_tables(connection, cursor)

    qt.graphic()

    data.close(connection)

main()