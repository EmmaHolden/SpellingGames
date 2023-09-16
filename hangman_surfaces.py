import pygame
pygame.init()
from game_variables import chalk_font_60, chalk_font_60_underlined, chalk_font_120

class HangmanSurfaces():
    def __init__(self):
        self.background = pygame.image.load('graphics/chalkboard.jpg').convert_alpha()
        self.background = pygame.transform.scale(self.background, (1200, 700))
        self.instructions_title = chalk_font_60_underlined.render('How To Play Hangman:', False, "white")
        self.start_instructions = chalk_font_60_underlined.render('Press Space Bar to Play', False, "white")
        self.word_was_label = chalk_font_60.render('The  word  was :', False, "white")
        self.line_horizontal_surface = pygame.image.load('graphics/line.png').convert_alpha()
        self.line_horizontal_surface = pygame.transform.scale(self.line_horizontal_surface, (620, 50))
        self.line_vertical_surface = pygame.image.load('graphics/line.png').convert_alpha()
        self.line_vertical_surface = pygame.transform.scale(self.line_vertical_surface, (300, 50))
        self.line_vertical_surface = pygame.transform.rotate(self.line_vertical_surface, 90)

    def draw_grid(self, screen):
        screen.blit(self.line_horizontal_surface, (60, 320))
        screen.blit(self.line_horizontal_surface, (60, 390))
        screen.blit(self.line_horizontal_surface, (60, 460))
        screen.blit(self.line_vertical_surface, (145, 260))
        screen.blit(self.line_vertical_surface, (225, 260))
        screen.blit(self.line_vertical_surface, (305, 260))
        screen.blit(self.line_vertical_surface, (385, 260))
        screen.blit(self.line_vertical_surface, (465, 260))
        screen.blit(self.line_vertical_surface, (545, 260))

    def get_current_word(self, letter_objects):
        word = ""
        for object in letter_objects:
            if object.revealed:
                word += object.name
            else:
                word += "_"
            word += " "
        return chalk_font_120.render(word, False, "white")


    def get_current_picture(self, guesses):
        hangman_surface = pygame.image.load(f'graphics/washingman{guesses}.png').convert_alpha()
        return pygame.transform.scale(hangman_surface, (400, 400))

    def get_win_lose_message(self, guesses):
        if guesses == 9:
            message = 'Y O U     L O S E!'
        else:
            message = 'Y O U     W I N!'
        return chalk_font_120.render(message, False, "white")


