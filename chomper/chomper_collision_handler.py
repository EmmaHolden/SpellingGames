import pygame
from chomper.chomper_enemy import Enemy
class CollisionHandler():

    def __init__(self, game, enemy_group, chomper, food, teleporter_group):
        self.game = game
        self.enemy_group = enemy_group
        self.chomper = chomper
        self.food = food
        self.teleporter_group = teleporter_group
    def check_food_collision(self):
        if pygame.sprite.groupcollide(self.chomper, self.food, False, False):
            self.game.current_letter_index += 1
            self.game.display.reveal_word()
            self.game.score.increase_score(10)
            if self.game.current_letter_index < len(self.game.spelling_word):
                self.chomper.sprite.grow()
                self.chomper.sprite.increase_speed(1)
                self.food.sprite.relocate_food()
                for item in self.enemy_group:
                    if item.letter == self.game.spelling_word[self.game.current_letter_index]:
                        item.update_letter()
                self.enemy_group.add(Enemy(self.game))
            else:
                self.game.game_over()
    def check_enemy_collision(self):
        collision = pygame.sprite.groupcollide(self.chomper, self.enemy_group, False, True)
        if collision:
            self.chomper.sprite.harmful_collision()

    def check_which_teleporter(self):
        for teleporter in self.teleporter_group:
            if teleporter.rect.colliderect(self.chomper.sprite.rect):
                return teleporter
    def check_teleporter_collision(self):
        collisions =  pygame.sprite.groupcollide(self.chomper, self.teleporter_group, False, False)
        if collisions:
            self.game.score.increase_score(2)
            self.chomper.sprite.increase_speed(0.25)
            teleporter = self.check_which_teleporter()
            self.chomper.sprite.direction = teleporter.position
            self.chomper.sprite.rect.x = self.chomper.sprite.find_new_x_coordinate(teleporter)
            self.chomper.sprite.rect.y = self.chomper.sprite.find_new_y_coordinate(teleporter)


    def check_collisions(self):
        self.check_food_collision()
        self.check_enemy_collision()
        self.check_teleporter_collision()