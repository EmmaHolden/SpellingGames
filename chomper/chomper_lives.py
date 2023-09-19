import pygame
class Lives():
    def __init__(self, game):
        self.game = game
        self.lives = 3
        self.get_lives_display()
    def get_lives_display(self):
        self.lives_display = pygame.image.load(f'graphics/heart{self.lives}.png').convert_alpha()

    def decrease_lives(self):
        self.lives -= 1