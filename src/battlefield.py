from PySide6.QtWidgets import QWidget, QGridLayout

from src.cardcontroller import CardController
from src.cardwidget import CardWidget


class BattleField(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def set_deck(self, deck):
        layout = QGridLayout()
        index = 0
        for i in range(5):
            for j in range(3):
                if index >= len(deck):
                    break
                layout.addWidget(deck[index], i, j)
                index += 1

        self.setLayout(layout)
