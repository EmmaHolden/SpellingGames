from horse_racing_horse_class import Horse
import random
class PlayerHorse(Horse):
    def __init__(self, y_coordinate, colour):
        super().__init__(y_coordinate, colour)

    def update(self):
        random_num = random.randint(0, 50)
        if random_num % 3 != 0:
            self.move_forward()
        elif random_num == 1:
            self.make_slower()
        self.increase_animation_counter()