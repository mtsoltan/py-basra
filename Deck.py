from card_constants import *
from Card import Card
import random

SHUFFLE_COUNT = 100


class Deck():
    def __init__(self):
        self.cards = []
        self.regenerate()

    def regenerate(self):
        self.cards = []
        for i in range(CARD_COUNT):
            self.cards.append(Card(card_id=i))

    def shuffle(self, shuffle_count: int = SHUFFLE_COUNT):
        temp = None

        for i in range(shuffle_count):
            rnd1 = random.randint(0, 51)
            rnd2 = random.randint(0, 51)
            temp = self.cards[rnd1]
            self.cards[rnd1] = self.cards[rnd2]
            self.cards[rnd2] = temp
