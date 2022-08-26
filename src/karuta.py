import csv
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QLabel, QPushButton, QVBoxLayout

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
        # Todo: ゲームをする前の状態を作る
        # Startbutton 設置して、押したらゲームスタート
        # 終わったらまた、スタートに戻る。

        self.start_button = QPushButton('&Start', self)
        self.start_button.clicked.connect(self.start)
        self.abort_button = QPushButton('&Abort', self)
        self.abort_button.hide()

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.start_button)
        self.setLayout(self.layout)

        path = '../data/4letters.csv'
        self.data = read(path)

    def ready(self):
        user_card_controller = CardController(self.data[0:7], self.check_answer, self)
        self.battle_field = BattleField(user_card_controller, self)

        host_card_controller = CardController(self.data[0:7], parent=self)
        self.host_field = HostField(host_card_controller, self)
        self.answer_correct.connect(self.host_field.next)

        self.layout.addWidget(self.battle_field)
        self.battle_field.hide()
        self.layout.addWidget(self.host_field)
        self.host_field.hide()
        self.host_field.host_cards_empty.connect(self.reset_to_start)

    def start(self):
        self.ready()
        self.battle_field.ready_to_start()
        self.host_field.ready_to_start()
        self.battle_field.show()
        self.host_field.show()
        self.start_button.hide()

    def reset_to_start(self):
        self.host_field.hide()
        self.battle_field.hide()
        # del self.host_field, self.battle_field
        self.start_button.show()


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
