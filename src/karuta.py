import csv
import random
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QLabel, QPushButton, QVBoxLayout

from src.battlefield import BattleField
import cardcontroller
from src.cardwidget import CardWidget
from src.hostfield import HostField


class Karuta(QWidget):
    answer_correct = Signal()
    answer_wrong = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        path = '../data/4letters.csv'
        self.data = []
        self.data = read(path)

        self.start_button = QPushButton('&Start', self)
        self.start_button.clicked.connect(self.start)
        self.abort_button = QPushButton('&Abort', self)
        self.abort_button.hide()

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.start_button)
        self.setLayout(self.layout)

    def ready(self):
        using_data = random.sample(self.data, 7)
        battle_deck = cardcontroller.create_deck(data=using_data, clicked_action=self.check_answer)
        self.battle_field = BattleField(battle_deck, parent=self)

        random.shuffle(using_data)
        self.question_deck = cardcontroller.create_deck(using_data)
        self.host_field = HostField(self.question_deck.pop(), self)

        self.layout.addWidget(self.battle_field)
        self.battle_field.hide()
        self.layout.addWidget(self.host_field)
        self.host_field.hide()
        self.host_field.host_cards_empty.connect(self.reset_to_start)

    def start(self):
        self.ready()
        self.battle_field.ready_to_start()
        self.battle_field.show()
        self.host_field.show()
        self.start_button.hide()

    def reset_to_start(self):
        self.host_field.hide()
        self.battle_field.hide()
        self.start_button.show()

    @Slot(QWidget)
    def check_answer(self, answer: CardWidget):
        self.battle_field.setDisabled(True)
        if answer == self.host_field.question:
            answer.setDisabled(True)
            self.battle_field.setDisabled(False)
            self.next_question()
            self.answer_correct.emit()
        else:
            print(answer._main_text)
            self.battle_field.setDisabled(False)
            self.answer_wrong.emit()

    def next_question(self):
        try:
            self.host_field.deal(self.question_deck.pop())
        except IndexError:
            self.host_field.end()
            self.battle_field.end()
            self.reset_to_start()


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
