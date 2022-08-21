import random

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGridLayout

from src.fieldview import FieldView


class HostField(FieldView):
    host_cards_empty = Signal()

    def __init__(self, card_controller, parent=None):
        super().__init__(card_controller, parent)
        self.question = None
        self.layout = QGridLayout()

    def ready_to_start(self):
        # Todo: card が available なっていない。
        if self._deck is None:
            self.card_controller.reset()
            self._deck = self.card_controller.create_deck()
        random.shuffle(self._deck)
        self.question = self._deck.pop()
        self.question.show()
        self.deal(self.question)

    def deal(self, w):
        self.layout.addWidget(w, 1, 1)
        self.setLayout(self.layout)

    def next(self):
        previous = self.question
        previous.hide()
        try:
            self.question = self._deck.pop()
        except IndexError:
            self._deck = None
            self.host_cards_empty.emit()
        self.layout.replaceWidget(previous, self.question)
