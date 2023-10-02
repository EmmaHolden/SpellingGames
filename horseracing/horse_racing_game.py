import pygame
import random
import pyttsx3
from scene_base import SceneBase
from game_variables import spelling_words
from horseracing.horse_racing_text_input_box import TextInputBox
from horseracing.horse_racing_computer_horse import ComputerHorse
from horseracing.horse_racing_player_horse import PlayerHorse
from horseracing.horse_racing_results import HorseRacingResults

class HorseGame(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.finished_places = []
        self.background = pygame.image.load('graphics/horseracingbackground.png')
        self.text_speech = pyttsx3.init()
        self.race_active = True
        self.counter = 0
        self.text_input_box = TextInputBox(self)
        self.player_horse = pygame.sprite.GroupSingle()
        self.player_horse.add(PlayerHorse(340, "pink", self))
        self.challenger_horses = pygame.sprite.Group()
        self.challenger_horses.add(ComputerHorse(420, "blue", self))
        self.challenger_horses.add(ComputerHorse(520, "red", self))
        self.challenger_horses.add(ComputerHorse(620, "orange", self))

    def check_spelling(self, spelling_attempt):
        if spelling_attempt.strip().lower() == self.spelling_word.lower():
            self.player_horse.sprite.make_faster()
        else:
            self.player_horse.sprite.make_slower()
        self.counter = 0
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.text_input_box.active:
                    self.text_input_box.handle_typing(event)
                else:
                    if event.key == pygame.K_SPACE:
                        if not self.player_horse.sprite.check_finished():
                            self.counter += 1
                            if self.counter == 20:
                                self.race_active = False
                                self.text_input_box.make_active()
                                self.spelling_word = random.choice(spelling_words)
                                print(self.spelling_word )
                                self.text_speech.say(self.spelling_word)
                                self.text_speech.runAndWait()

    def Update(self):
        if self.race_active:
            if len(self.finished_places) < 4:
                if self.player_horse.sprite.check_finished():
                    if self.player_horse.sprite not in self.finished_places:
                        self.finished_places.append(self.player_horse.sprite)
                else:
                    self.player_horse.update()
                for horse in self.challenger_horses:
                    if horse.check_finished():
                        if horse not in self.finished_places:
                            self.finished_places.append(horse)
                    else:
                        horse.update()
            else:
                for horse in self.finished_places:
                    print(horse.colour)
                self.SwitchToScene(HorseRacingResults(self.finished_places))
    def Render(self, screen):
        screen.blit(self.background, (0, 0))
        self.player_horse.draw(screen)
        self.challenger_horses.draw(screen)
        pygame.draw.rect(screen, self.text_input_box.colour, self.text_input_box.rect)
        screen.blit(self.text_input_box.image, (self.text_input_box.rect.x + 5, self.text_input_box.rect.y + 5))