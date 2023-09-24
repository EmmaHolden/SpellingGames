import random
from horse_racing_horse_class import Horse
class ComputerHorse(Horse):
    def __init__(self, y_coordinate, colour):
        super().__init__(y_coordinate, colour)

    def update(self):
        random_num = random.randint(0, 9)
        if random_num % 3 != 0:
            self.move_forward()
        if random_num in [0, 1]:
            self.make_faster()
        if random_num in [2, 3]:
            self.make_slower()
        self.increase_animation_counter()
