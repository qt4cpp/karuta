import csv
import random

from src.cardwidget import CardWidget


class CardController:
    def __init__(self, data, f=None):
        self._data = data
        self._deck = []
        self._f = f

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
            self._deck[-1].clicked.connect(self._f)
        return self._deck

    def shuffle(self):
        random.shuffle(self._deck)
