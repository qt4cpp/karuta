from PySide6.QtCore import Signal, QObject

from src.cardwidget import CardWidget


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
