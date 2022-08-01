import random

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGridLayout

from src.fieldview import FieldView


class HostField(FieldView):
    host_cards_empty = Signal()

    def __init__(self, card_controller, parent=None):
        super().__init__(card_controller, parent)
        self.question = None

    def ready_to_start(self):
        random.shuffle(self._deck)
        self.question = self._deck.pop()
        self.deal(self.question)

    def deal(self, w):
        layout = QGridLayout()
        layout.addWidget(w, 1, 1)
        self.setLayout(layout)

    def next(self):
        previous = self.question
        try:
            self.question = self._deck.pop()
        except IndexError:
            self.host_cards_empty.emit()
        self.layout().replaceWidget(previous, self.question)
        previous.hide()