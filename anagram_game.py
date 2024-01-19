import pygame
import random
from scene_base import SceneBase
from game_variables import spelling_words, anagram_font_100


box_coordinates = [(100, 100), (200, 100), (300, 100), (400, 100), (500, 100), (600, 100), (700, 100), (800, 100), (900, 100), (1000, 100), (1100, 100)]

class Letters(pygame.sprite.Sprite):
    def __init__(self, name, coordinates):
        super().__init__()
        self.name = name
        self.home_coordinates = coordinates
        self.image = anagram_font_100.render(name, False, "black")
        self.rect = self.image.get_rect(topleft = self.home_coordinates)
    def check_collision(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            print("You touched me:")
            print(self.name)
            print(self.home_coordinates)

    def update(self, mouse_pos):
        self.check_collision(mouse_pos)
class AnagramGame(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.background = pygame.image.load('graphics/babywallpaper.jpg')
        self.spelling_word = random.choice(spelling_words).upper()
        self.letter_group = pygame.sprite.Group()
        self.display_letters()

    def display_letters(self):
        for i in range(0, len(self.spelling_word)):
            print(self.spelling_word)
            print(i)
            self.letter_group.add(Letters(name = self.spelling_word[i], coordinates = box_coordinates[i]))

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.letter_group.update(event.pos)

    def Update(self):
        pass

    def Render(self, screen):
        screen.blit(self.background, (0, 0))
        self.letter_group.draw(screen)
