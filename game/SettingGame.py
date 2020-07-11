class SettingGame:
    def __init__(self, WIDTH, HEIGHT, LEFT_TOP_CORNER, LEFT_BOT_CORNER,
                 RIGHT_TOP_CORNER, RIGHT_BOT_CORNER, paddle_speed=10, ball_speed=5, ball_size=30, paddle_r_size=1000,
                 paddle_size=100,
                 ai_number=0,
                 max_score=100, max_game_duration=10 ** 4,
                 random_reflection=0):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.paddle_speed = paddle_speed
        self.ball_speed = ball_speed
        self.ball_size = ball_size
        self.paddle_r_size = paddle_r_size
        self.paddle_size = paddle_size
        self.ai_number = ai_number
        self.max_score = max_score
        self.max_game_duration = max_game_duration
        self.random_reflection = random_reflection
        self.LEFT_TOP_CORNER = LEFT_TOP_CORNER
        self.LEFT_BOT_CORNER = LEFT_BOT_CORNER
        self.RIGHT_TOP_CORNER = RIGHT_TOP_CORNER
        self.RIGHT_BOT_CORNER = RIGHT_BOT_CORNER
