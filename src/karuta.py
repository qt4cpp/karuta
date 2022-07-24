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

        self.data = []
        path = '../data/4letters.csv'
        self.data = read(path)

        user_card_controller = CardController(self.data, self.check_answer)
        self.battle_field = BattleField(user_card_controller.create_deck())

        host_card_controller = CardController(self.data)
        self.host_field = HostField(host_card_controller.create_deck())

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


def read(path):
    data = []
    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


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
