import pygame
from game_variables import horse_font_40

active_colour = "white"
inactive_colour = "#A7ECFF"
class TextInputBox():
    def __init__(self, game):
        self.game = game
        self.rect = pygame.Rect(450, 50, 200, 50)
        self.active = False
        self.text = ""
        self.colour = active_colour if self.active else inactive_colour
        self.image = horse_font_40.render(self.text, True, "black", self.colour)
    def make_active(self):
        self.active = True
        self.colour = active_colour
    def make_inactive(self):
        self.active = False
        self.colour = inactive_colour
    def handle_typing(self, event):
        if event.key == pygame.K_RETURN:
            self.game.check_spelling(self.text.strip())
            self.text = ''
            self.make_inactive()
            self.game.race_active = True
            self.colour = inactive_colour
        elif event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            if len(self.text) <= 30:
                self.text += event.unicode.upper()
        self.image = horse_font_40.render(self.text, True, "black")
        width = max(200, self.image.get_width() + 20)
        self.rect.w = width