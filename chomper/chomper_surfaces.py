import pygame
from game_variables import pixel_font_60, game_colours

class ChomperSurfaces():
    def __init__(self, game):
        self.game = game
        self.title = pixel_font_60.render('Chomper', False, "black")
        self.background = pygame.Surface((1200, 700))
        self.background.fill(game_colours["green"])
        self.play_grid = pygame.Surface((1050, 550))
        self.play_grid.fill(game_colours["yellow"])
        self.word_surface = pixel_font_60.render("Word:", False, "black")
        self.revealed_letter_surface = pixel_font_60.render("", False, game_colours["yellow"])

    def get_game_timer(self, screen):
        timer_display = pixel_font_60.render(f'{round(self.game.game_timer / 60)}', False, "black")
        screen.blit(timer_display, (160, 20))

    def reveal_word(self):
        self.revealed_letters = self.game.spelling_word[0:self.game.current_letter_index]
        self.revealed_letter_surface = pixel_font_60.render(self.revealed_letters, False, game_colours["yellow"])

    def update(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.play_grid, (75, 75))
        screen.blit(self.title, (520, 20))
        screen.blit(self.game.lives.lives_display, (800, 10))
        screen.blit(self.game.score.score_display, (300, 650))
        screen.blit(self.word_surface, (700, 645))
        screen.blit(self.revealed_letter_surface, (820, 645))
        self.get_game_timer(screen)
