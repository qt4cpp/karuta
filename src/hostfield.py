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

    def ready_to_start(self):
        # self.next()
        pass

    def deal(self, w):
        l = self.layout().addWidget(w)
        self.setLayout(l)