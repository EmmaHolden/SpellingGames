import pygame
from scene_base import SceneBase
from anagram_game import AnagramGame

class AnagramInstructions(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.background = pygame.image.load('graphics/babywallpaper.jpg')

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.SwitchToScene(AnagramGame())

    def Update(self):
        pass

    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.blit(self.background, (0, 0))