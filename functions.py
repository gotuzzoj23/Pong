import sys
import pygame
from time import sleep


def check_events(ball, paddle_player, paddle_ai, play_button, stats, sb):
    """Respond to keypresses"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddle_player)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddle_player)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, ball, paddle_player, paddle_ai, mouse_x,
                              mouse_y, sb)


def check_keydown_events(event, paddle_player):
    """Respond to keypresses"""
    if event.key == pygame.K_UP:
        paddle_player.moving_up = True
    elif event.key == pygame.K_DOWN:
        paddle_player.moving_down = True
    elif event.key == pygame.K_LEFT:
        paddle_player.moving_left = True
    elif event.key == pygame.K_RIGHT:
        paddle_player.moving_right = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, paddle_player):
    if event.key == pygame.K_UP:
        paddle_player.moving_up = False
    elif event.key == pygame.K_DOWN:
        paddle_player.moving_down = False
    elif event.key == pygame.K_LEFT:
        paddle_player.moving_left = False
    elif event.key == pygame.K_RIGHT:
        paddle_player.moving_right = False


def check_play_button(stats, play_button, ball, paddle_player, paddle_ai, mouse_x, mouse_y, sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:
        # Reset game settings.
        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        sb.prep_score_player()
        sb.prep_score_ai()

        paddle_player.center_paddles()
        paddle_ai.center_paddles()
        ball.center_ball()


def update_screen(pong_settings, screen, ball, paddle_player, paddle_ai, play_button, stats, sb):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop.
    screen.fill(pong_settings.bg_color)
    play_button.draw_line()
    ball.blit_me()
    paddle_player.blit_me()
    paddle_ai.blit_me()

    sb.show_score()
    check_winner(play_button, stats)
    if not stats.game_active:
        play_button.draw_bg()
        play_button.draw_button()

    pygame.display.flip()


def ball_update(pong_settings, ball, paddle_player, paddle_ai, stats, sb):
    check_boundaries(pong_settings, ball, paddle_player, paddle_ai, stats)
    ball.update()
    sb.prep_score_player()
    sb.prep_score_ai()
    check_ball_paddle_collision(ball, paddle_player, paddle_ai)


def paddle_player_update(paddle_player):
    paddle_player.update()


def paddle_ai_update(pong_settings, ball, paddle_ai):
    # Computer paddles will head back to center while the ball is on the player's half of table
    if ball.rect.centerx > (pong_settings.screen_width / 2):
        if paddle_ai.center_vert < (pong_settings.screen_height / 2):
            paddle_ai.center_vert += pong_settings.paddle_speed_factor
        if paddle_ai.center_vert > (pong_settings.screen_height / 2):
            paddle_ai.center_vert -= pong_settings.paddle_speed_factor
        if paddle_ai.center_hor1 < (pong_settings.screen_width / 4):
            paddle_ai.center_hor1 += pong_settings.paddle_speed_factor
            paddle_ai.center_hor2 += pong_settings.paddle_speed_factor
        if paddle_ai.center_hor1 > (pong_settings.screen_width / 4):
            paddle_ai.center_hor1 -= pong_settings.paddle_speed_factor
            paddle_ai.center_hor2 -= pong_settings.paddle_speed_factor

    # Computer paddles will ball while it's on the computer's side of the table
    if ball.rect.centerx <= (pong_settings.screen_width / 2):
        if (paddle_ai.center_vert < ball.rect.centery) and (
                paddle_ai.image_vert_rec.bottom < pong_settings.screen_height):
            paddle_ai.center_vert += pong_settings.paddle_speed_factor
        if (paddle_ai.center_vert > ball.rect.centery) and (paddle_ai.image_vert_rec.top > 0):
            paddle_ai.center_vert -= pong_settings.paddle_speed_factor
        if (paddle_ai.center_hor1 < ball.rect.centerx) and (paddle_ai.image_hor1_rect.right < 600):
            paddle_ai.center_hor1 += pong_settings.paddle_speed_factor
            paddle_ai.center_hor2 += pong_settings.paddle_speed_factor
        if (paddle_ai.center_hor1 > ball.rect.centerx) and (paddle_ai.image_hor1_rect.left > 0):
            paddle_ai.center_hor1 -= pong_settings.paddle_speed_factor
            paddle_ai.center_hor2 -= pong_settings.paddle_speed_factor

    paddle_ai.image_vert_rec.centery = paddle_ai.center_vert
    paddle_ai.image_hor1_rect.centerx = paddle_ai.center_hor1
    paddle_ai.image_hor2_rect.centerx = paddle_ai.center_hor2


def reset_paddles(paddle_player, paddle_ai, ball):
    paddle_player.center_paddles()
    paddle_ai.center_paddles()
    ball.directionx = 1
    ball.directiony = 1


def check_ball_paddle_collision(ball, paddle_player, paddle_ai):
    collision = pygame.Rect.colliderect(paddle_player.image_vert_rec, ball)
    if collision:
        ball.directionx *= -1.0
        hit()
    collision = pygame.Rect.colliderect(paddle_player.image_hor1_rect, ball)
    if collision:
        hit()
        ball.directiony *= -1.0
    collision = pygame.Rect.colliderect(paddle_player.image_hor2_rect, ball)
    if collision:
        hit()
        ball.directiony *= -1.0
    collision = pygame.Rect.colliderect(paddle_ai.image_vert_rec, ball)
    if collision:
        ball.directionx *= -1.0
        hit()
    collision = pygame.Rect.colliderect(paddle_ai.image_hor1_rect, ball)
    if collision:
        ball.directiony *= -1.0
        hit()
    collision = pygame.Rect.colliderect(paddle_ai.image_hor2_rect, ball)
    if collision:
        ball.directiony *= -1.0
        hit()


def check_winner(button, stats):
    if stats.score_player == 7:
        stats.winner_announce += 1
        button.prep_winner("WINNER, WINNER, CHICKEN DINNER Player 1 WINS")
        if stats.winner_announce == 1:
            player1_winner()
        stats.game_active = False
        pygame.mouse.set_visible(True)
    if stats.score_ai == 7:
        stats.winner_announce += 1
        button.prep_winner("AI WINS, TRY HARDER")
        if stats.winner_announce == 1:
            ai_winner()
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_boundaries(pong_settings, ball, paddle_player, paddle_ai, stats):
    if ball.rect.left > pong_settings.screen_width or ball.rect.right > pong_settings.screen_width:
        ball.center_ball()
        stats.score_ai += 1
        goal()
        sleep(1)
        reset_paddles(paddle_player, paddle_ai, ball)
    if ball.rect.right < 0 or ball.rect.left < 0:
        ball.center_ball()
        stats.score_player += 1
        goal()
        sleep(1)
        reset_paddles(paddle_player, paddle_ai, ball)
    if ball.rect.bottom >= pong_settings.screen_height or ball.rect.top >= pong_settings.screen_height:
        if ball.rect.centerx < (pong_settings.screen_width / 2):
            stats.score_player += 1
            goal()
        if ball.rect.centerx > (pong_settings.screen_width / 2):
            stats.score_ai += 1
            goal()
        ball.center_ball()
        sleep(1)
        reset_paddles(paddle_player, paddle_ai, ball)
    if ball.rect.bottom <= 0 or ball.rect.top <= 0:
        if ball.rect.centerx < (pong_settings.screen_width / 2):
            stats.score_player += 1
            goal()
        if ball.rect.centerx > (pong_settings.screen_width / 2):
            stats.score_ai += 1
            goal()
        ball.center_ball()
        sleep(1)
        reset_paddles(paddle_player, paddle_ai, ball)


def goal():
    game_over_audio = pygame.mixer.Sound("sounds/goal.ogg")
    game_over_audio.set_volume(1.0)
    pygame.mixer.Sound.play(game_over_audio)


def hit():
    game_over_audio = pygame.mixer.Sound("sounds/hit.ogg")
    game_over_audio.set_volume(1.0)
    pygame.mixer.Sound.play(game_over_audio)


def player1_winner():
    game_over_audio = pygame.mixer.Sound("sounds/player1_winner.ogg")
    game_over_audio.set_volume(1.0)
    pygame.mixer.Sound.play(game_over_audio)


def ai_winner():
    game_over_audio = pygame.mixer.Sound("sounds/ai_winner.ogg")
    game_over_audio.set_volume(1.0)
    pygame.mixer.Sound.play(game_over_audio)
