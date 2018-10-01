class GameStats:
    def __init__(self, pong_settings):
        """Initialize statistics."""
        self.pong_settings = pong_settings
        self.reset_stats()
        self.game_active = False
        self.score_player = 0
        self.score_ai = 0
        self.winner_announce = 0

    def reset_stats(self):
        self.score_player = 0
        self.score_ai = 0
        self.winner_announce = 0
