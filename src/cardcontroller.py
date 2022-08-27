from PySide6.QtCore import Signal, QObject

from src.cardwidget import CardWidget


class CardController(QObject):
    set_reset_deck = Signal()

    def __init__(self, data, clicked_action=None, reset_action=None, parent=None):
        super().__init__(parent)
        self._data = data
        self._deck = None
        self.clicked_action = clicked_action
        self.reset_action = reset_action

    def pick(self, index):
        return self._data[index]

    def data(self):
        return self._data

    @staticmethod
    def create_deck(data, amount=0, clicked_action=None):
        if amount:
            deck_size = min(amount, len(data))
        else:
            deck_size = len(data)
        deck = []
        for i in range(deck_size):
            c = data[i]
            deck.append(CardWidget(c[0], c[1]))
            if clicked_action is not None:
                deck[-1].clicked.connect(clicked_action)
        return deck
