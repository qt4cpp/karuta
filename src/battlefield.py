import random

from src.fieldview import FieldView


class BattleField(FieldView):
    def __init__(self, card_controller, parent=None):
        super().__init__(card_controller, parent)

    def ready_to_start(self):
        random.shuffle(self._deck)
        self.deal(5, 3)
