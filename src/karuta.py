import csv
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget

from src.battlefield import BattleField
from src.cardcontroller import CardController
from src.cardwidget import CardWidget
from src.hostfield import HostField


class Karuta(QWidget):
    answer_correct = Signal()
    answer_wrong = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        controller = CardController('../data/4letters.csv', self.check_answer)
        controller.read()

        self.battle_field = BattleField(controller.create_deck())
        # self.battle_field.deal(5, 3)

        # 問題を出す
        self.host_field = HostField(controller.create_deck())
        # self.host_field.deal(1,1)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.host_field)
        self.layout.addWidget(self.battle_field)
        self.setLayout(self.layout)

        self.answer_correct.connect(self.host_field.next)

        self.start()

    def start(self):
        self.host_field.ready_to_start()
        self.battle_field.ready_to_start()

    @Slot(QWidget)
    def check_answer(self, answer: CardWidget):
        self.battle_field.setDisabled(True)
        if answer == self.host_field.question:
            answer.setDisabled(True)
            self.battle_field.setDisabled(False)
            self.answer_correct.emit()
        else:
            print(answer._main_text)
            self.battle_field.setDisabled(False)
            self.answer_wrong.emit()


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
