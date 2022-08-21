from PySide6.QtCore import Signal, QObject

from src.cardwidget import CardWidget


class CardController(QObject):
    set_reset_deck = Signal()

    def __init__(self, data, clicked_action=None, reset_action=None):
        super().__init__()
        self._data = data
        self._deck = None
        self.clicked_action = clicked_action
        self.reset_action = reset_action

    def pick(self, index):
        return self._data[index]

    def data(self):
        return self._data

    def create_deck(self, amount=0):
        if amount:
            deck_size = min(amount, len(self._data))
        else:
            deck_size = len(self._data)
        self._deck = []
        for i in range(deck_size):
            c = self.pick(i)
            self._deck.append(CardWidget(c[0], c[1]))
            if self.clicked_action is not None:
                self._deck[-1].clicked.connect(self.clicked_action)
                self.set_reset_deck.connect(self._deck[-1].reset)
        return self._deck

    def reset(self):
        self.set_reset_deck.emit()
