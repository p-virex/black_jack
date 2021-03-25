import pygame

from constants import RANK_INDEX_NAME, COLOUR_INDEX_NAME


class Card(pygame.sprite.Sprite):
    def __init__(self, colour, rank):
        pygame.sprite.Sprite.__init__(self)
        """
        :param colour:  масть карты от 0 до 3
        :param rank:  ранг карты от 1 до 13
        """
        self.__colour = colour
        self.__rank = rank
        self.__name_card = '{}_of_{}'.format(RANK_INDEX_NAME[rank], COLOUR_INDEX_NAME[colour])
        image = pygame.image.load(f'res\\{self.name}.png')
        self.image = pygame.transform.scale(image, (100, 150))  # 100 x 150 scale 5
        self.rect = self.image.get_rect()
        self.image.set_alpha(0)

    @property
    def rank(self):
        return self.__rank

    @property
    def colour(self):
        return self.__colour

    @property
    def name(self):
        return self.__name_card

    def set_position(self, pos):
        self.rect.x, self.rect.y = pos

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return self.name


class DeckBackOfCard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('res\\back_of_a_card.png')
        self.image = pygame.transform.scale(image, (100, 150))  # 100 x 150 scale 5
        self.rect = self.image.get_rect()

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True