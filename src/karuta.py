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
        self.start_button.clicked.connect(self.ready)
        self.abort_button = QPushButton('&Abort', self)
        self.abort_button.hide()

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.start_button)
        self.setLayout(self.layout)

        path = '../data/4letters.csv'
        self.data = read(path)

        user_card_controller = CardController(self.data, self.check_answer)
        self.battle_field = BattleField(user_card_controller)

        host_card_controller = CardController(self.data)
        self.host_field = HostField(host_card_controller)
        self.answer_correct.connect(self.host_field.next)
        self.host_field.host_cards_empty.connect(self.reset_to_start)

    def ready(self):
        self.start_button.hide()
        self.start()

    def start(self):
        self.battle_field.ready_to_start()
        self.layout.addWidget(self.battle_field)
        self.host_field.ready_to_start()
        self.layout.addWidget(self.host_field)

    def reset_to_start(self):
        self.battle_field.hide()
        self.host_field.hide()
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
