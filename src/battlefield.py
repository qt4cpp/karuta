import random

from PySide6.QtWidgets import QWidget, QGridLayout

from src.fieldview import FieldView


class BattleField(QWidget):
    def __init__(self, card_controller, parent=None):
        super().__init__(parent)
        self.field = FieldView(card_controller, parent)
        l = QGridLayout()
        l.addWidget(self.field)
        self.setLayout(l)

    def ready_to_start(self):
        random.shuffle(self.field._deck)
        self.field.deal(5, 3)
