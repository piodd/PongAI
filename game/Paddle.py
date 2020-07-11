

class Paddle:
    def __init__(self, pos_x, pos_y, speed_y, r_size, size):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed_y = speed_y
        self.r_size = r_size
        self.size = size

    def make_move(self, move: str):
        if move == "Up":
            self.pos_y -= self.speed_y
        elif move == "Down":
            self.pos_y += self.speed_y
