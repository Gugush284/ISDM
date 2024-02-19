from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class TableWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Таблица оборудования")

        button = QPushButton("Press Me!")

        self.setMinimumSize(QSize(400, 400))

        self.setCentralWidget(button)


def graphic():
    app = QApplication(sys.argv)

    window = TableWindow()
    window.show()

    app.exec()