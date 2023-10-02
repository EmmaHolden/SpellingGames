import pygame
from scene_base import SceneBase
from horseracing.horse_racing_game import HorseGame
from game_variables import game_colours, horse_font_30, horse_font_60

instructions_list = ['When the race starts, rapidly press space bar repeatedly as your horse runs.',
                     'When you hear a spelling word spoken, a text box will appear.',
                     'Correctly type the word and press ENTER.',
                     'Correct spellings make your horse speed up!']

instruction_coordinates = [(600, 200), (600, 300), (600, 400), (600, 500)]
class HorseRacingInstructions(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.title = horse_font_60.render('Horse Racing Spellings', False, "black")
        self.title_rect = self.title.get_rect(center=(600, 80))
        self.green_surface = pygame.Surface((1200, 400))
        self.green_surface.fill(game_colours["grassgreen"])
        self.start_instructions = horse_font_60.render('Press Space Bar to Play', False, 100)
        self.start_instructions_rect = self.start_instructions.get_rect(center=(600, 620))
        self.instructions = []
        self.instructions_rect = []
        for i in range(0, len(instructions_list)):
            instruction_surface = horse_font_30.render(instructions_list[i], False, "black")
            instruction_rect = instruction_surface.get_rect(center = instruction_coordinates[i])
            self.instructions.append(instruction_surface)
            self.instructions_rect.append(instruction_rect)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.SwitchToScene(HorseGame())

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill(game_colours["skyblue"])
        screen.blit(self.green_surface, (0, 150))
        pygame.draw.line(screen, "white", (0, 150), (1200, 150), 10)
        pygame.draw.line(screen, "white", (0, 250), (1200, 250), 10)
        pygame.draw.line(screen, "white", (0, 350), (1200, 350), 10)
        pygame.draw.line(screen, "white", (0, 450), (1200, 450), 10)
        pygame.draw.line(screen, "white", (0, 550), (1200, 550), 10)
        screen.blit(self.title, self.title_rect)
        screen.blit(self.start_instructions, self.start_instructions_rect)
        for i in range(0, len(self.instructions)):
            screen.blit(self.instructions[i], self.instructions_rect[i])

