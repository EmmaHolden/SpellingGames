import pygame
import random
from scene_base import SceneBase
from chomper.chomper_game import ChomperGame
from game_variables import spelling_words, pixel_font_60, pixel_font_80, pixel_font_120, game_colours
import pyttsx3
class ChomperDisplayWord(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.spelling_word = random.choice(spelling_words).upper()
        self.text_speech = pyttsx3.init()
        self.timer = 180
        self.spelling_word_label_surface = pixel_font_60.render("Spelling Word: ", False, "black")
        self.spelling_word_label_rect = self.spelling_word_label_surface.get_rect(center=(600, 100))
        self.spelling_word_display = pixel_font_80.render(f'{self.spelling_word}', False, "black")
        self.spelling_word_display_rect = self.spelling_word_display.get_rect(center=(600, 350))


    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.text_speech.say(self.spelling_word)
                self.text_speech.runAndWait()
    def Update(self):
        self.timer_display = pixel_font_120.render(f'{round(self.timer / 60)}', False, "black")
        self.timer_rect = self.timer_display.get_rect(center=(600, 550))
        self.timer -= 1
        if self.timer <= 0:
            self.SwitchToScene(ChomperGame(self.spelling_word))

    def Render(self, screen):
        screen.fill(game_colours["orange"])
        screen.blit(self.timer_display, self.timer_rect)
        screen.blit(self.spelling_word_label_surface, self.spelling_word_label_rect)
        screen.blit(self.spelling_word_display, self.spelling_word_display_rect)