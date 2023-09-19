import pygame
from scene_base import SceneBase
from chomper.chomper_display_word import ChomperDisplayWord
from game_variables import game_colours, pixel_font_40, pixel_font_60

instructions_list = [
    'Move the chomper around the screen to catch the letters.',
    'Be careful of enemy letters sent to confuse you!',
    'Pressing space bar stops the game and lets you hear the word.',
    'Purple teleporters give extra points but make the chomper faster.',
    'Do not touch the walls!'
                          ]
instruction_coordinates = [(600, 180), (600, 260), (600, 340), (600, 420), (600, 500)]
class ChomperInstructions(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.title = pixel_font_60.render('Chomper', False, "black")
        self.title_rect = self.title.get_rect(center=(600, 100))
        self.start_instructions = pixel_font_60.render('Press Space Bar to Play', False, 100)
        self.start_instructions_rect = self.start_instructions.get_rect(center=(600, 600))
        self.instructions = []
        self.instructions_rect = []
        for i in range(0, len(instructions_list)):
            instruction_surface = pixel_font_40.render(instructions_list[i], False, "black")
            instruction_rect = instruction_surface.get_rect(center = instruction_coordinates[i])
            self.instructions.append(instruction_surface)
            self.instructions_rect.append(instruction_rect)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.SwitchToScene(ChomperDisplayWord())

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill(game_colours["lightblue"])
        screen.blit(self.title, self.title_rect)
        screen.blit(self.start_instructions, self.start_instructions_rect)
        for i in range(0, len(self.instructions)):
            screen.blit(self.instructions[i], self.instructions_rect[i])



