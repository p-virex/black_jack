import pygame

from colors import WHITE, BLACK
from constants import MEDIUM_TRANSPARENCY, NOT_TRANSPARENCY
from fonts import ELEPHANT_FONT_M


class Button(pygame.Surface):
    def __init__(self, size, coord, color=WHITE, text=None, text_coord=(0, 0), font=ELEPHANT_FONT_M, color_text=BLACK):
        super(Button, self).__init__(size)
        self.text = text
        self.text_coord = text_coord
        self.font = font
        self.text_color = color_text
        self.rect = self.get_rect()
        self.rect.x, self.rect.y = coord
        self.fill(color)
        self.set_alpha(100)

    def render_text(self):
        if self.text:
            text = self.font.render(self.text, True, self.text_color)
            self.blit(text, self.text_coord)

    def check_click(self, mouse_pos, event):
        if self.rect.collidepoint(mouse_pos):
            event()

    def check_mouse_alpha(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.set_alpha(NOT_TRANSPARENCY)
        else:
            self.set_alpha(MEDIUM_TRANSPARENCY)

    def change_color(self, color):
        self.fill(color)
