import random

from src.fieldview import FieldView


class BattleField(FieldView):
    def __init__(self, deck, parent=None):
        super().__init__(deck, parent)

    def ready_to_start(self):
        random.shuffle(self._deck)
        self.deal(5, 3)
