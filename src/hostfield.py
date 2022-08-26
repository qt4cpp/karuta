import random

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGridLayout, QWidget

from src.fieldview import FieldView


class HostField(QWidget):
    host_cards_empty = Signal()

    def __init__(self, card_controller, parent=None):
        super().__init__(parent)
        self.field = FieldView(card_controller, parent)
        self.question = None
        l = QGridLayout()
        self.setLayout(l)

    def ready_to_start(self):
        random.shuffle(self.field._deck)
        self.next()

    def deal(self, w):
        l = self.layout().addWidget(w)
        self.setLayout(l)

    def next(self):
        previous = self.question
        if previous is not None:
            previous.hide()
        try:
            self.question = self.field._deck.pop()
        except IndexError:
            self.field._deck = None
            self.question = None
            self.host_cards_empty.emit()
        else:
            self.deal(self.question)