from PySide6.QtWidgets import QWidget, QGridLayout

from src.cardwidget import CardWidget


class BattleField(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QGridLayout()
        layout.addWidget(CardWidget('絶体絶命', 'ぜったいぜつめい'), 0, 0)
        layout.addWidget(CardWidget('危機一髪', 'ききいっぱつ'), 0, 1)
        layout.addWidget(CardWidget('自画自賛', 'じがじさん'), 1, 0)
        layout.addWidget(CardWidget('自業自得', 'じごうじとく'), 1, 1)

        self.setLayout(layout)
