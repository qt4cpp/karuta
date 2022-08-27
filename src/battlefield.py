import random

from PySide6.QtWidgets import QWidget, QGridLayout

from src.fieldview import FieldView


class BattleField(QWidget):
    def __init__(self, deck, parent=None):
        super().__init__(parent)
        self.deck = deck

    def ready_to_start(self):
        random.shuffle(self.deck)
        self.deal(5, 3)

    def deal(self, x, y):
        l = QGridLayout()
        index = 0
        for i in range(x):
            for j in range(y):
                if index >= len(self.deck):
                    break
                l.addWidget(self.deck[index], i, j)
                index += 1
        self.setLayout(l)

    def end(self):
        pass