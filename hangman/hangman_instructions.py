import pygame
from game_variables import chalk_font_40
from scene_base import SceneBase
from hangman.hangman_game import HangmanGame
from hangman.hangman_surfaces import HangmanSurfaces

instructions_list = ['- One of your spelling words will be chosen randomly.',
                     '- On the screen you will see an empty "_" for every letter in the word.',
                     '- Type or click on a letter with your mouse to guess.',
                     '- If you guess a letter correctly, that letter will be revealed.',
                     '- If it is not in the word, a piece of the hangman picture will be drawn.',
                     '- To win, guess the word before the man finishes hanging his washing out.']

instruction_coordinates = [(90, 180), (90, 240), (90, 300), (90, 360), (90, 420), (90, 480)]
class HangmanInstructions(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.display = HangmanSurfaces()
        self.instructions = []
        for instruction in instructions_list:
            instruction_surface = chalk_font_40.render(instruction.upper(), False, "white")
            self.instructions.append(instruction_surface)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.SwitchToScene(HangmanGame(self.display))

    def Update(self):
        pass

    def Render(self, screen):
        screen.blit(self.display.background, (0, 0))
        screen.blit(self.display.instructions_title, (400, 100))
        for i in range(0, len(instructions_list)):
            screen.blit(self.instructions[i], instruction_coordinates[i])
        screen.blit(self.display.start_instructions, (380, 530))
