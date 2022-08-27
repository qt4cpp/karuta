from PySide6.QtWidgets import QWidget, QGridLayout


class FieldView(QWidget):
    def __init__(self, deck, parent=None):
        super().__init__(parent)
        self.deck = deck

    def deal(self, x, y):
        layout = QGridLayout()
        index = 0
        for i in range(x):
            for j in range(y):
                if index >= len(self.deck):
                    break
                layout.addWidget(self.deck[index], i, j)
                index += 1
        self.setLayout(layout)
