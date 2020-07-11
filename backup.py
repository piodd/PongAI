def create_paddle_py_image(self, paddle_r, player_nr):
    if player_nr == 1:
        paddle_image = Image.new("RGBA", (self.paddle_r, self.paddle_r))
        paddle_draw = ImageDraw.Draw(paddle_image)
        paddle_draw.pieslice((0, 0, self.paddle_r, self.paddle_r), 0, 360, fill=COLOR_PADDLE)
        cut = (
            self.paddle_r - self.paddle_r * 0.1, self.paddle_r // 3, self.paddle_r,
            self.paddle_r - self.paddle_r // 3)
        paddle_image = paddle_image.crop(cut)
        paddle_image = self.resize_image(0.3, paddle_image)
        mode = paddle_image.mode
        size = paddle_image.size
        self.paddle_image_1_size_y = size[1]
        data = paddle_image.tobytes()
        paddle_image = pygame.image.fromstring(data, size, mode)
    else:
        paddle_image = Image.new("RGBA", (self.paddle_r, self.paddle_r))
        paddle_draw = ImageDraw.Draw(paddle_image)
        paddle_draw.pieslice((0, 0, self.paddle_r, self.paddle_r), 0, 360, fill=COLOR_PADDLE)
        cut = (0, self.paddle_r // 3, self.paddle_r * 0.1, self.paddle_r - self.paddle_r // 3)
        paddle_image = paddle_image.crop(cut)
        paddle_image = self.resize_image(0.3, paddle_image)
        mode = paddle_image.mode
        size = paddle_image.size
        self.paddle_image_2_size_y = size[1]
        data = paddle_image.tobytes()
        paddle_image = pygame.image.fromstring(data, size, mode)
    return paddle_image



    def board_collision_check_paddle(self, paddle: Paddle):
        if paddle.pos_y - paddle.size // 2 < self.min_y:
            paddle.pos_y = self.min_y + paddle.size // 2
        elif paddle.pos_y + paddle.size // 2 > self.max_y:
            paddle.pos_y = self.max_y - paddle.size // 2

    def make_ai_move():
        decision_1 = ai_decision(game.give_info_for_net_1(), ai_player_1)
        decision_2 = ai_decision(game.give_info_for_net_2(), ai_player_2)
        global player_1_move
        global player_2_move
        if decision_1[0] > 0:
            player_1_move = "Up"
        elif decision_1[1] > 0:
            player_1_move = "Down"
        else:
            player_1_move = "Static"
        if decision_2[0] > 0:
            player_2_move = "Up"
        elif decision_2[1] > 0:
            player_2_move = "Down"
        else:
            player_2_move = "Static"