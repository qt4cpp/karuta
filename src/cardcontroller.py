import csv
import random

from src.cardwidget import CardWidget


class CardController:
    def __init__(self, path):
        self._data = []
        self._deck = []
        self._path = path

    def read(self):
        with open(self._path) as file:
            reader = csv.reader(file)
            for row in reader:
                self._data.append(row)

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
        return self._deck

    def shuffle(self):
        random.shuffle(self._deck)
