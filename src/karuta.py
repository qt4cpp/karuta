import csv
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget

from src.battlefield import BattleField
from src.cardcontroller import CardController
from src.cardwidget import CardWidget
from src.hostfield import HostField


class Karuta(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        controller = CardController('../data/4letters.csv', self.check_answer)
        controller.read()

        battle_field = BattleField()
        battle_field.set_deck(controller.create_deck())

        # 問題を出す
        host_field = HostField()
        host_field.set_host_card(controller.create_deck())

        self.layout = QHBoxLayout()
        self.layout.addWidget(host_field)
        self.layout.addWidget(battle_field)
        self.setLayout(self.layout)

    @Slot(QWidget)
    def check_answer(self, card: CardWidget):
        print(card._main_text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        karuta = Karuta()
        self.setCentralWidget(karuta)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    w = MainWindow()
    w.show()

    sys.exit(app.exec())
