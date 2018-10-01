# Paddle Pong game created by Jose Gotuzzo

import pygame
from settings import Settings
import functions as funct
from ball import Ball
from paddle import Paddle_player
from paddle_ai import Paddle_ai
from game_stats import GameStats
from start_button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize Pygame
    pygame.init()

    # Settings
    pong_settings = Settings()
    screen = pygame.display.set_mode((pong_settings.screen_width, pong_settings.screen_height))

    play_button = Button(pong_settings, screen, "PLAY")
    stats = GameStats(pong_settings)
    sb = Scoreboard(pong_settings, screen, stats)

    pygame.display.set_caption("PONG")
    ball = Ball(pong_settings, screen)
    paddle_player = Paddle_player(pong_settings, screen)
    paddle_ai = Paddle_ai(pong_settings, screen)

    # Start main loop
    while True:
        funct.check_events(ball, paddle_player, paddle_ai, play_button, stats, sb)
        if stats.game_active:
            funct.ball_update(pong_settings, ball, paddle_player, paddle_ai, stats, sb)
            funct.paddle_player_update(paddle_player)
            funct.paddle_ai_update(pong_settings, ball, paddle_ai)
        funct.update_screen(pong_settings, screen, ball, paddle_player, paddle_ai, play_button, stats, sb)


run_game()
