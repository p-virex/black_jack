import pygame

from colors import WHITE, GREEN_TABLE
from constants import HIGH_TRANSPARENCY, VERY_LOW_TRANSPARENCY


class Player(object):
    def __init__(self, name, bank=1000):
        self.hand = pygame.sprite.Group()
        self.name = name
        self.score = 0
        self.bank = bank
        self.hand_surface = pygame.Surface((800, 200))
        self.hand_surface.fill(GREEN_TABLE)
        # self.hand_surface.set_alpha(VERY_LOW_TRANSPARENCY)

    def clear_hand(self):
        self.hand.empty()
        self.hand_surface = pygame.Surface((800, 200))
        self.hand_surface.fill(GREEN_TABLE)

    def add_cart(self, card):
        if card:
            card.rect.x = 110 * len(self.hand)
            card.image.set_alpha(20)
            self.hand.add(card)
        self.get_score()

    def get_score(self):
        self.score = 0
        for card in self.hand:
            rank = card.rank
            if card.name.startswith('ace'):# and self.score >= 20:
                if self.score > 11 and self.score < 21:
                    rank = 1
            self.score += rank


