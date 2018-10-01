from typing import Optional, Any

import pygame.font


class Scoreboard:
    """A class to report scoring information."""
    score_image_ai: Optional[Any]
    score_ai_rect: object
    score_player_rect: object
    score_image_player: Optional[Any]

    def __init__(self, pong_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pong_settings = pong_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score_player()
        self.prep_score_ai()

    def prep_score_player(self):
        """Turn the score into a rendered image."""
        score = int(self.stats.score_player)
        score_str = "{:,}".format(score)
        self.score_image_player = self.font.render(score_str, True, self.text_color, self.pong_settings.bg_color)

        # Display the score at the top right of the screen
        self.score_player_rect = self.score_image_player.get_rect()
        self.score_player_rect.right = self.screen_rect.right - 20
        self.score_player_rect.top = 20

    def prep_score_ai(self):
        """Turn the score into a rendered image."""
        score = int(self.stats.score_ai)
        score_str = "{:,}".format(score)
        self.score_image_ai = self.font.render(score_str, True, self.text_color, self.pong_settings.bg_color)

        # Display the score at the top left of the screen
        self.score_ai_rect = self.score_image_ai.get_rect()
        self.score_ai_rect.right = self.screen_rect.left + 20
        self.score_ai_rect.top = 20

    def show_score(self):
        """Draw score and ships to the screen."""
        self.screen.blit(self.score_image_player, self.score_player_rect)
        self.screen.blit(self.score_image_ai, self.score_ai_rect)
