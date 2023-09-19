import pygame
from game_variables import pixel_font_60
class Scorekeeper():
    def __init__(self, game):
        self.game = game
        self.score = 0
        self.get_score_display()
    def get_score_display(self):
        self.score_display = pixel_font_60.render(f'Score:  {self.score}', False, "black")
    def increase_score(self, amount):
        self.score += amount
        self.get_score_display()

