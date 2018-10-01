class Settings:
    """A class to store all setting for Pong"""

    def __init__(self):
        """Initialize game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Paddle settings
        self.paddle_speed_factor = 2.0
        self.paddle_color = (255, 255, 255)
        self.paddle_vert_height = 100
        self.paddle_vert_width = 20
        self.paddle_hor_width = 100
        self.paddle_hor_height = 20

        # Ball settings
        self.ball_speed_factor = 1.0
        self.ball_color = (255, 255, 255)
        self.width = 10
        self.ball_width = 10

        self.score_limit = 7
