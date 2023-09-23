import pygame
import random
import pyttsx3
from scene_base import SceneBase
from game_variables import pixel_font_60, spelling_words

active_colour = "white"
inactive_colour = "green"
class Horse(pygame.sprite.Sprite):
    def __init__(self, y_coordinate, colour):
        super().__init__()
        self.colour = colour
        self.animation_counter = 0
        self.current_speed_index = 0
        self.speeds = [(0, 1), (0, 2), (1, 2)]
        self.y_coordinate = y_coordinate
        self.image = pygame.image.load(f'graphics/{self.colour}horsey{self.animation_counter}.png')
        self.x_pos = 70
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_coordinate))

    def make_faster(self):
        if self.current_speed_index < len(self.speeds) - 1:
            self.current_speed_index += 1
    def make_slower(self):
        if self.current_speed_index > 0:
            self.current_speed_index -= 1
    def move_forward(self):
        current_speed = (self.speeds[self.current_speed_index])
        random_step = random.randint(current_speed[0], current_speed[1])
        self.x_pos += random_step
    def increase_animation_counter(self):
        if self.animation_counter >= 3:
            self.animation_counter = 0
        else:
            self.animation_counter += 0.1
        self.image = pygame.image.load(f'graphics/{self.colour}horsey{round(self.animation_counter)}.png')
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_coordinate))

class PlayerHorse(Horse):
    def __init__(self, y_coordinate, colour):
        super().__init__(y_coordinate, colour)

    def update(self):
        if random.randint(0, 1) == 1:
            self.move_forward()
        self.increase_animation_counter()

class ComputerHorse(Horse):
    def __init__(self, y_coordinate, colour):
        super().__init__(y_coordinate, colour)

    def update(self):
        random_num = random.randint(0, 9)
        if random_num in [0, 1, 2, 3, 4]:
            self.move_forward()
            if random_num in [0, 1]:
                self.make_faster()
        else:
            if random_num in [5, 6]:
                self.make_slower()
        self.increase_animation_counter()

class TextInputBox():
    def __init__(self, game):
        self.game = game
        self.rect = pygame.Rect(450, 50, 200, 50)
        self.active = False
        self.text = ""
        self.colour = active_colour if self.active else inactive_colour
        self.image = pixel_font_60.render(self.text, True, "black", self.colour)
    def make_active(self):
        self.active = True
        self.colour = active_colour
    def make_inactive(self):
        self.active = False
        self.colour = inactive_colour
    def handle_typing(self, event):
        if event.key == pygame.K_RETURN:
            self.game.check_spelling(self.text)
            self.text = ''
            self.make_inactive()
            self.game.race_active = True
            self.colour = inactive_colour
        elif event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            if len(self.text) <= 30:
                self.text += event.unicode
        self.image = pixel_font_60.render(self.text, True, "black")
        width = max(200, self.image.get_width() + 10)
        self.rect.w = width
class HorseGame(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.text_speech = pyttsx3.init()
        self.race_active = True
        self.text_input_box = TextInputBox(self)
        self.player_horse = pygame.sprite.GroupSingle()
        self.player_horse.add(PlayerHorse(200, "pink"))
        self.challenger_horses = pygame.sprite.Group()
        self.challenger_horses.add(ComputerHorse(350, "blue"))
        self.challenger_horses.add(ComputerHorse(500, "red"))
        self.challenger_horses.add(ComputerHorse(650, "orange"))

    def check_spelling(self, spelling_attempt):
        if spelling_attempt.lower() == self.spelling_word.lower():
            self.player_horse.sprite.make_faster()
        else:
            self.player_horse.sprite.make_slower()
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.text_input_box.active:
                    self.text_input_box.handle_typing(event)
    def Update(self):
        if self.race_active:
            self.player_horse.update()
            self.challenger_horses.update()
            random_spelling_chance = random.randint(0, 400)
            if random_spelling_chance == 1:
                self.race_active = False
                self.text_input_box.make_active()
                self.spelling_word = random.choice(spelling_words)
                self.text_speech.say(self.spelling_word)
                self.text_speech.runAndWait()
    def Render(self, screen):
        screen.fill("green")
        self.player_horse.draw(screen)
        self.challenger_horses.draw(screen)
        pygame.draw.rect(screen, self.text_input_box.colour, self.text_input_box.rect)
        screen.blit(self.text_input_box.image, (self.text_input_box.rect.x + 5, self.text_input_box.rect.y + 5))