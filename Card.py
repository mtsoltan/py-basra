from card_constants import *
from typing import Optional


class Card:
    def __init__(self, _value: Optional[int] = None, _type: Optional[int] = None, card_id: Optional[int] = None):
        if card_id is None:
            self.value = _value
            self.type = _type
            return
        self.type = card_id // VALUE_COUNT
        self.value = card_id % VALUE_COUNT

    def __repr__(self):
        return str(self.get_id())

    def get_type(self):
        return self.type

    def get_value(self):
        return self.value

    def get_name(self):
        return VALUES[self.value] + ' of ' + TYPES[self.type]

    def get_id(self):
        return self.value + self.type * VALUE_COUNT
