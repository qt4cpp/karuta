from PySide6.QtWidgets import QWidget, QGridLayout

from src.cardwidget import CardWidget


class HostField(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._deck = []
        self.layout = QGridLayout()

    def set_host_card(self, card: CardWidget):
        self.layout.addWidget(card[0])
        self.setLayout(self.layout)
