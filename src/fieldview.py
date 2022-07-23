from PySide6.QtWidgets import QWidget, QGridLayout


class FieldView(QWidget):
    def __init__(self, parent=None, deck=None):
        super().__init__(parent)
        self._deck = deck

    def set_deck(self, deck):
        self._deck = deck

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
