from random import shuffle, randint

from card import Card
from constants import COLOUR_INDEX, RANK_NAME_INDEX


class Deck:
    def __init__(self):
        self.__card_deck = list()

    def make_deck(self):
        for color in COLOUR_INDEX:
            for rank in RANK_NAME_INDEX.values():
                self.__card_deck.append(Card(color, rank))

    def shuffle_deck(self):
        shuffle(self.__card_deck)

    @property
    def get_deck(self):
        return self.__card_deck

    def return_card_in_deck(self, card):
        position = randint(0, self.get_len_deck)
        self.__card_deck.insert(position, card)

    @property
    def get_card(self):
        if self.__card_deck:
            return self.__card_deck.pop()

    @property
    def get_len_deck(self):
        return len(self.__card_deck)

    def return_card(self, card, pos=0):
        self.__card_deck.insert(pos, card)
