from scene_base import SceneBase
import pygame
from game_variables import pixel_font_60, pixel_font_80, game_colours

class ChomperResults(SceneBase):
    def __init__(self, spelling_word, lives, score, timer):
        SceneBase.__init__(self)
        self.spelling_word = spelling_word
        self.lives = lives
        self.timer = timer
        self.score = score
        self.title = pixel_font_60.render('Chomper', False, "black")
        self.title_rect = self.title.get_rect(center=(600, 100))
        self.end_message = self.get_end_message()
        self.end_message_rect = self.end_message.get_rect(center=(600, 250))
        self.spelling_word_surface = pixel_font_60.render(f"Spelling Word: {self.spelling_word}", False, "black")
        self.spelling_word_rect = self.spelling_word_surface.get_rect(center=(600, 400))
        self.score_surface = pixel_font_60.render(f"Score: {self.score}", False, "black")
        self.score_rect = self.score_surface.get_rect(center=(600, 550))
    def get_end_message(self):
        if self.lives < 1:
            return pixel_font_60.render('Oops! You ran out of lives!', False, "black")
        elif self.timer <= 0:
            return pixel_font_60.render('Oops! You ran out of time!', False, "black")
        else:
            return pixel_font_60.render('Well done! You got all of the letters!', False, "black")


    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill(game_colours["lightblue"])
        screen.blit(self.title, self.title_rect)
        screen.blit(self.end_message, self.end_message_rect)
        screen.blit(self.spelling_word_surface, self.spelling_word_rect)
        screen.blit(self.score_surface, self.score_rect)


