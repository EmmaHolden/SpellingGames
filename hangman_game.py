import pygame
import string
import random
from scene_base import SceneBase
from hangman_letters import letter_coordinates, LetterButton, SecretLetter
from game_variables import spelling_words
from hangman_results import HangmanResults

class HangmanGame(SceneBase):
    def __init__(self, display):
        SceneBase.__init__(self)
        self.display = display
        self.letter_coordinates = letter_coordinates
        self.guessed_letters = []
        self.guesses = 0
        self.letters = list(string.ascii_uppercase)
        self.spelling_word = random.choice(spelling_words).upper()
        self.letter_objects = [SecretLetter(char) for char in self.spelling_word]
        self.letter_button_group = pygame.sprite.Group()
        self.add_letter_objects()
        self.update_current_picture()
        self.update_current_word_surface()

    def update_current_picture(self):
        self.current_picture = self.display.get_current_picture(self.guesses)
    def update_current_word_surface(self):
        self.current_word_surface = self.display.get_current_word(self.letter_objects)
    def add_letter_objects(self):
        for i in range(0, 26):
            self.letter_button_group.add(LetterButton(game = self, name=self.letters[i], coordinates=self.letter_coordinates[i]))

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.unicode.isalpha():
                self.check_guess(event.unicode)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.letter_button_group.update(event.pos)

    def Update(self):
        pass


    def check_guess(self, event_key):
        guess = event_key.upper()
        if guess not in self.guessed_letters:
            self.guessed_letters.append(guess)
            for i in self.letter_button_group:
                if i.name == guess:
                    i.kill()
            if guess in self.spelling_word:
                for letter in self.letter_objects:
                    if guess == letter.name:
                        letter.revealed = True
                        revealed = [letter.revealed for letter in self.letter_objects]
                        if False not in revealed:
                            self.SwitchToScene(HangmanResults(self.guesses, self.spelling_word, self.display))
                self.update_current_word_surface()
            else:
                self.guesses += 1
                self.update_current_picture()
                if self.guesses == 9:
                    self.SwitchToScene(HangmanResults(self.guesses, self.spelling_word, self.display))

    def Render(self, screen):
        screen.blit(self.display.background, (0, 0))
        self.letter_button_group.draw(screen)
        self.display.draw_grid(screen)
        screen.blit(self.current_picture, (700, 200))
        screen.blit(self.current_word_surface, (300, 100))

