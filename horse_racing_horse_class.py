import pygame
import random
class Horse(pygame.sprite.Sprite):
    def __init__(self, y_coordinate, colour):
        super().__init__()
        self.colour = colour
        self.animation_counter = 0
        self.current_speed_index = 0
        self.speeds = [(0, 1), (0, 2), (1, 2), (1, 3)]
        self.y_coordinate = y_coordinate
        self.image = pygame.image.load(f'graphics/{self.colour}horsey{self.animation_counter}.png')
        self.x_pos = 70
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_coordinate))

    def make_faster(self):
        if self.current_speed_index < len(self.speeds) - 1:
            self.current_speed_index += 1
    def make_slower(self):
        if self.current_speed_index > 0:
            self.current_speed_index -= 1
    def move_forward(self):
        current_speed = (self.speeds[self.current_speed_index])
        random_step = random.randint(current_speed[0], current_speed[1])
        self.x_pos += random_step
    def increase_animation_counter(self):
        if self.animation_counter >= 3:
            self.animation_counter = 0
        else:
            self.animation_counter += 0.1
        self.image = pygame.image.load(f'graphics/{self.colour}horsey{round(self.animation_counter)}.png')
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_coordinate))