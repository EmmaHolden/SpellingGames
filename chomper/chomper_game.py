import pygame
from itertools import product
from scene_base import SceneBase
from chomper.chomper_teleporter import Teleporter
from chomper.chomper_lives import Lives
from chomper.chomper_monster import Chomper
from chomper.chomper_collision_handler import CollisionHandler
from chomper.chomper_scorekeeper import Scorekeeper
from chomper.chomper_food import Food
from chomper.chomper_surfaces import ChomperSurfaces
from chomper.chomper_results import ChomperResults
import pyttsx3

x_coordinates = [110, 170, 230, 290, 350, 410, 470, 530, 590, 650, 710, 770, 830, 890, 950, 1010, 1070]

y_coordinates = [100, 160, 220, 280, 340, 400, 460, 520, 580]
class ChomperGame(SceneBase):
    def __init__(self, spelling_word):
        SceneBase.__init__(self)
        self.text_speech = pyttsx3.init()
        self.spelling_word = spelling_word
        self.game_timer = 3600
        self.coordinates = list(product(x_coordinates, y_coordinates))
        self.current_letter_index = 0
        self.display = ChomperSurfaces(self)
        self.score = Scorekeeper(self)
        self.lives = Lives(self)
        self.chomper = pygame.sprite.GroupSingle()
        self.food = pygame.sprite.GroupSingle()
        self.enemy_group = pygame.sprite.Group()
        self.teleport_group = pygame.sprite.Group()
        self.collision_handler = CollisionHandler(self, self.enemy_group, self.chomper, self.food, self.teleport_group)
        self.start_game_add_to_groups()
    def start_game_add_to_groups(self):
        self.chomper.add(Chomper(self))
        self.food.add(Food(self))
        left_teleporter = Teleporter("left")
        right_teleporter = Teleporter("right")
        top_teleporter = Teleporter("up")
        bottom_teleporter = Teleporter("down")
        left_teleporter.get_opposite(right_teleporter)
        top_teleporter.get_opposite(bottom_teleporter)
        self.teleport_group.add(left_teleporter, right_teleporter, top_teleporter, bottom_teleporter)

    def game_over(self):
        self.SwitchToScene(ChomperResults(self.spelling_word, self.lives.lives, self.score.score, self.game_timer))

    def reduce_timer(self):
        self.game_timer -= 1
        if self.game_timer <= 0:
            self.game_over()
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.text_speech.say(self.spelling_word)
                    self.text_speech.runAndWait()
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    self.chomper.sprite.change_direction()
    def Update(self):
        if self.chomper.sprite.hurt == True:
            self.chomper.sprite.timed_injury()
        self.chomper.sprite.move()
        self.collision_handler.check_collisions()
        self.reduce_timer()

    def Render(self, screen):
        self.display.update(screen)
        self.enemy_group.draw(screen)
        self.teleport_group.draw(screen)
        self.chomper.draw(screen)
        self.food.draw(screen)

