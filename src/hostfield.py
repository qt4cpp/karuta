import random

from PySide6.QtWidgets import QGridLayout

from src.fieldview import FieldView


class HostField(FieldView):
    def __init__(self, deck, parent=None):
        super().__init__(deck, parent)
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
        self.question = self._deck.pop()
        self.layout().replaceWidget(previous, self.question)
        previous.hide()