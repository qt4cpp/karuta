import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from src.battlefield import BattleField
from src.cardwidget import CardWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setCentralWidget(BattleField(self))


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    w = MainWindow()
    w.show()

    sys.exit(app.exec())
