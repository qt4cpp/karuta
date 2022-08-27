import random

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGridLayout, QWidget

from src.fieldview import FieldView


class HostField(QWidget):
    host_cards_empty = Signal()

    def __init__(self, w, parent=None):
        super().__init__(parent)
        self.question = w
        l = QGridLayout()
        l.addWidget(self.question)
        self.setLayout(l)

    def deal(self, w):
        if self.question is not None:
            previous = self.question
            previous.hide()
        self.question = w
        l = self.layout().replaceWidget(previous, self.question)

    def end(self):
        self.question.hide()
        self.question = None