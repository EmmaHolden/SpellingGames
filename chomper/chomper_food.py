import pygame
import random
from game_variables import pixel_font_60

class Food(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pixel_font_60.render(self.check_letter(), False, 40)
        self.location = random.choice(self.game.coordinates)
        self.game.coordinates.remove(self.location)
        self.rect = self.image.get_rect(topleft= self.location)

    def check_letter(self):
        try:
            return self.game.spelling_word[self.game.current_letter_index]
        except IndexError:
            self.game.game_active = False

    def relocate_food(self):
        self.location = random.choice(self.game.coordinates)
        self.game.coordinates.remove(self.location)
        self.rect.x = self.location[0]
        self.rect.y = self.location[1]
        self.image = pixel_font_60.render(self.check_letter(), False, 40)
