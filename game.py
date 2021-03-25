import pygame as pg

from button import Button
from card import DeckBackOfCard
from colors import GREEN_TABLE, BLACK
from constants import EUROPE, AMERICAN, NOT_TRANSPARENCY, MEDIUM_TRANSPARENCY, SIZE
from deck import Deck
from fonts import ELEPHANT_FONT_B, ARIAL_FONT_B, ARIAL_FONT_M
from player import Player


class BlackJack:

    def __init__(self):
        self.run_game = True
        self.is_menu = True
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption('Black Jack 1.0')
        self.clock = pg.time.Clock()
        self.deck = None
        self.player = None
        self.dealer = None
        self.back_card = None
        self.type_game = EUROPE
        self.winner = None
        self.rate = None
        self.change_rate = None
        self.player = Player('Player')

    def init_menu(self):
        self.button_start = Button((170, 40), (30, 30), text='Start game')
        self.button_easy = Button((170, 40), (30, 80), text='Europe')
        self.button_hard = Button((170, 40), (30, 130), text='American')
        self.button_exit = Button((170, 40), (30, 180), text='Exit game')
        menu_bg = pg.image.load('res\\bg.jpg')
        self.menu_bg = pg.transform.scale(menu_bg, SIZE)

    def init_game(self):
        self.button_return_to_menu = Button((250, 40), (10, 10), text='Return')
        self.button_new_game = Button((250, 40), (10, 60), text='Start new game')
        self.button_hit_me = Button((250, 40), (10, 120), text='Hit me')
        self.button_stop = Button((250, 40), (10, 170), text='Stop')
        self.button_rate_up = Button((150, 40), (10, 220), text='+10 coins')
        self.button_rate_down = Button((150, 40), (10, 340), text='-10 coins')

    def init_new_game(self):
        self.winner = None
        self.change_rate = True
        self.rate = 10
        self.player.bank -= 10
        self.deck = Deck()
        self.deck.make_deck()
        self.deck.shuffle_deck()
        self.player.clear_hand()
        print(self.player.hand)
        self.dealer = Player('Dealer')
        self.back_card = DeckBackOfCard()
        self.player.add_cart(self.deck.get_card)
        self.player.add_cart(self.deck.get_card)
        self.check_black_jack()
        if self.type_game == AMERICAN:
            cart = self.deck.get_card
            self.dealer.add_cart(cart)

    def render_game(self):
        self.screen.fill(GREEN_TABLE)
        self.screen.blit(self.button_return_to_menu, self.button_return_to_menu.rect)
        self.screen.blit(self.button_new_game, self.button_new_game.rect)

        self.button_return_to_menu.render_text()
        self.button_new_game.render_text()

        if self.deck and self.player and self.dealer:
            self.screen.blit(self.button_hit_me, self.button_hit_me.rect)
            self.screen.blit(self.button_stop, self.button_stop.rect)
            self.screen.blit(self.button_rate_up, self.button_rate_up.rect)
            self.screen.blit(self.button_rate_down, self.button_rate_down.rect)

            self.button_hit_me.render_text()
            self.button_stop.render_text()
            self.button_rate_up.render_text()
            self.button_rate_down.render_text()
            self.screen.blit(self.back_card.image, (300, 10))
            self.screen.blit(self.player.hand_surface, (200, 380))
            self.screen.blit(self.dealer.hand_surface, (420, 10))
            self.player.hand.draw(self.player.hand_surface)
            self.dealer.hand.draw(self.dealer.hand_surface)
            score = f'YOU LOOS! Score: {self.player.score}' if self.player.score > 21 else self.player.score
            text = ARIAL_FONT_B.render(f'Player score: {score}', True, BLACK)
            self.screen.blit(text, (200, 300))
            score_dealer = ARIAL_FONT_B.render(f'Score dealer: {self.dealer.score}', True, BLACK)
            self.screen.blit(score_dealer, (200, 205))
            rate = ARIAL_FONT_M.render(f'Rate: {self.rate}', True, BLACK)
            self.screen.blit(rate, (10, 275))
            bank = ARIAL_FONT_M.render(f'Bank: {self.player.bank}', True, BLACK)
            self.screen.blit(bank, (10, 390))
            if self.winner:
                text = ARIAL_FONT_B.render(self.winner, True, BLACK)
                self.screen.blit(text, (540, 200))

    def render_menu(self):
        self.screen.blit(self.menu_bg, (0, 0))
        self.screen.blit(self.button_start, self.button_start.rect)
        self.screen.blit(self.button_exit, self.button_exit.rect)
        self.screen.blit(self.button_easy, self.button_easy.rect)
        self.screen.blit(self.button_hard, self.button_hard.rect)
        if self.type_game == EUROPE:
            self.button_easy.set_alpha(NOT_TRANSPARENCY)
            self.button_hard.set_alpha(MEDIUM_TRANSPARENCY)
        if self.type_game == AMERICAN:
            self.button_easy.set_alpha(MEDIUM_TRANSPARENCY)
            self.button_hard.set_alpha(NOT_TRANSPARENCY)
        self.button_start.render_text()
        self.button_exit.render_text()
        self.button_easy.render_text()
        self.button_hard.render_text()

    def start_game(self):
        while self.run_game is True:
            self.clock.tick(30)
            self.check_events()
            if self.is_menu is True:
                self.render_menu()
            else:
                self.render_game()
            pg.display.update()

    def check_events(self):
        for event in pg.event.get():
            if event.type is pg.QUIT:
                self.event_exit_game()
            if event.type == pg.MOUSEMOTION:
                self.render_button_select(event)
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if self.is_menu:
                    self.check_menu_events(event)
                else:
                    self.check_game_events(event)

    def check_black_jack(self):
        if self.player.score == 21:
            self.winner = f'WON PLAYER! Black Jack! {self.rate * 3}'
            self.player.bank += self.rate * 3

    def check_game_events(self, event):
        self.button_return_to_menu.check_click(event.pos, self.event_return_to_menu)
        self.button_new_game.check_click(event.pos, self.event_new_game)
        self.button_hit_me.check_click(event.pos, self.event_hit_me)
        self.button_stop.check_click(event.pos, self.event_turn_dealer)
        self.button_rate_up.check_click(event.pos, self.event_rate_up)
        self.button_rate_down.check_click(event.pos, self.event_rate_down)

    def render_button_select(self, event):
        if self.is_menu:
            self.button_start.check_mouse_alpha(event.pos)
            self.button_exit.check_mouse_alpha(event.pos)
        else:
            self.button_return_to_menu.check_mouse_alpha(event.pos)
            self.button_new_game.check_mouse_alpha(event.pos)
            self.button_hit_me.check_mouse_alpha(event.pos)
            self.button_stop.check_mouse_alpha(event.pos)
            self.button_rate_up.check_mouse_alpha(event.pos)
            self.button_rate_down.check_mouse_alpha(event.pos)

    def check_menu_events(self, event):
        self.button_hard.check_click(event.pos, self.event_hard_active)
        self.button_easy.check_click(event.pos, self.event_easy_active)
        self.button_start.check_click(event.pos, self.event_start_game)
        self.button_exit.check_click(event.pos, self.event_exit_game)

    def event_turn_dealer(self):
        self.change_rate = False
        if self.player.score <= 21:
            while self.dealer.score < 19:
                card = self.deck.get_card
                self.dealer.add_cart(card)
            if self.dealer.score <= 21 and self.dealer.score > self.player.score:
                self.winner = 'DEALER WON!'
            elif self.dealer.score == self.player.score:
                self.winner = 'PUSH! DEALER WON!'
            else:
                self.winner = f'PLAYER WON {self.rate * 2} COINS!'
                self.player.bank += self.rate * 2

    def event_rate_up(self):
        if self.change_rate:
            self.rate += 10
            self.player.bank -= 10

    def event_rate_down(self):
        if self.change_rate:
            self.rate -= 10
            self.player.bank += 10

    def event_new_game(self):
        self.init_new_game()

    def event_hit_me(self):
        if not self.winner:
            card = self.deck.get_card
            self.player.add_cart(card)

    def event_hard_active(self):
        self.type_game = AMERICAN

    def event_easy_active(self):
        self.type_game = EUROPE

    def event_return_to_menu(self):
        self.is_menu = True
        self.init_menu()

    def event_exit_game(self):
        self.run_game = False

    def event_start_game(self):
        self.is_menu = False
        self.init_game()


if __name__ == '__main__':
    game = BlackJack()
    game.init_menu()
    game.start_game()
