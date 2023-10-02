import pygame
from scene_base import SceneBase
from game_variables import horse_font_60

class HorseRacingResults(SceneBase):
    def __init__(self, finished_places):
        SceneBase.__init__(self)
        self.finished_places = finished_places
        self.background = pygame.image.load('graphics/horseraceresultsbackground.png')
        self.background = pygame.transform.scale(self.background, (1200, 700))
        for i in range(0, len(self.finished_places)):
            self.finished_places[i].image = pygame.transform.rotozoom(self.finished_places[i].image, 12, 1.2)
            horse_class = self.finished_places[i].__class__
            if horse_class.__name__ == "PlayerHorse":
                self.result_message = self.get_position(i)
        self.result_surface = horse_font_60.render(self.result_message, True, "black")
        self.result_rect = self.result_surface.get_rect(center = (600, 60))



    def get_position(self, index):
        if index == 0:
            return "Excellent job! You came 1st in the race!"
        elif index == 1:
            return "Well done! You came 2nd in the race."
        elif index == 2:
            return "Good try. You came 3rd in the race."
        else:
            return "You got 4th place. Better luck next time."

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.finished_places[0].image, (460, 290))
        screen.blit(self.finished_places[1].image, (220, 340))
        screen.blit(self.finished_places[2].image, (660, 400))
        screen.blit(self.finished_places[3].image, (810, 440))
        screen.blit(self.result_surface, self.result_rect)