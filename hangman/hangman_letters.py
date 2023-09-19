import pygame
from game_variables import chalk_font_60

letter_coordinates = [
    (120, 280), (200, 280), (280, 280), (360, 280), (440, 280), (520, 280), (600, 280),
    (120, 350), (200, 350), (280, 350), (360, 350), (440, 350), (520, 350), (600, 350),
    (120, 420), (200, 420), (280, 420), (360, 420), (440, 420), (520, 420), (600, 420),
                (200, 490), (280, 490), (360, 490), (440, 490), (520, 490),]

class LetterButton(pygame.sprite.Sprite):
    def __init__(self, game, name, coordinates):
        self.game = game
        super().__init__()
        self.name = name
        self.coordinates = coordinates
        self.image = chalk_font_60.render(name, False, "white")
        self.rect = self.image.get_rect(topleft = self.coordinates)
    def check_collision(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.game.check_guess(self.name)

    def update(self, mouse_pos):
        self.check_collision(mouse_pos)

class SecretLetter():
    def __init__(self, name):
        self.name = name
        self.revealed = False