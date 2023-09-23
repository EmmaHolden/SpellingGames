import pygame
from scene_base import SceneBase
from hangman.hangman_instructions import HangmanInstructions
from anagram_instructions import AnagramInstructions
from chomper.chomper_instructions import ChomperInstructions
from placeholder_scene import GameScene
from horse_racing_game import HorseGame


class MainMenu(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.letter_selected = None

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    self.SwitchToScene(self.get_chosen_game(event.unicode))

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((255, 0, 0))

    def get_chosen_game(self, letter):
        letter_selected = letter.upper()
        if letter_selected == "A":
            print("You chose Anagrams!")
            return AnagramInstructions()
        elif letter_selected == "H":
            print("You chose Hangman")
            return HangmanInstructions()
        elif letter_selected == "C":
            print("You chose Chomper!")
            return ChomperInstructions()
        elif letter_selected == "R":
            print("You chose horse racing!")
            return HorseGame()
        else:
            print("You chose a different letter!")
            return GameScene()