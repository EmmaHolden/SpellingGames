import pygame
from game_variables import chalk_font_120
from scene_base import SceneBase

class HangmanResults(SceneBase):
    def __init__(self, guesses, spelling_word, display):
        SceneBase.__init__(self)
        self.display = display
        self.guesses = guesses
        self.spelling_word = spelling_word
        self.spelling_word_surface = chalk_font_120.render(self.spelling_word, False, "white")
        self.win_lose_message = self.display.get_win_lose_message(self.guesses)
        self.hangman_surface = self.display.get_current_picture(self.guesses)


    def ProcessInput(self, events, pressed_keys):
        pass


    def Update(self):
        pass

    def Render(self, screen):
        screen.blit(self.display.background, (0, 0))
        screen.blit(self.hangman_surface, (700, 200))
        screen.blit(self.display.word_was_label, (200, 300))
        screen.blit(self.spelling_word_surface, (200, 400))
        screen.blit(self.win_lose_message, (300, 100))



