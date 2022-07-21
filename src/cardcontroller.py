import csv
import random

from src.cardwidget import CardWidget


class CardController:
    def __init__(self, path):
        self._data = []
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

    def create_deck(self, amount):
        deck_size = min(amount, len(self._data))
        random.shuffle(self._data)
        card_deck = []
        for i in range(deck_size):
            c = self.pick(i)
            card_deck.append(CardWidget(c[0], c[1]))
        return card_deck
