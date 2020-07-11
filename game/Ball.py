class Ball:
    def __init__(self, pos_x, pos_y, speed_x, speed_y, size):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.size = size

    def make_move(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
