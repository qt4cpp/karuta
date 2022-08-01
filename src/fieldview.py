from PySide6.QtWidgets import QWidget, QGridLayout

from src.cardcontroller import CardController


class FieldView(QWidget):
    def __init__(self, card_controller: CardController, parent=None):
        super().__init__(parent)
        self.card_controller = card_controller
        self._deck = card_controller.create_deck()

    def set_controller(self, card_controller: CardController):
        self.card_controller = card_controller
        self._deck = self.card_controller.create_deck()

    def deal(self, x, y):
        layout = QGridLayout()
        index = 0
        for i in range(x):
            for j in range(y):
                if index >= len(self._deck):
                    break
                layout.addWidget(self._deck[index], i, j)
                index += 1
        self.setLayout(layout)
