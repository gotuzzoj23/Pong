import pygame
from pygame.sprite import Sprite


class Paddle_ai(Sprite):

    def __init__(self, pong_settings, screen):
        """"Initlialize paddle attributes"""
        super(Paddle_ai, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.pong_settings = pong_settings
        self.color = pong_settings.paddle_color

        # Set the dimensions and properties for the horizontal paddle
        self.width_vert = pong_settings.paddle_vert_width
        self.height_vert = pong_settings.paddle_vert_height
        # Built the paddles's rect object
        self.image_vert_rec = pygame.Rect(0, 0, self.width_vert, self.height_vert)
        # Store a decimal value for the paddle's center
        self.image_vert_rec.centery = self.screen_rect.centery
        self.image_vert_rec.centerx = self.screen_rect.left + 15
        # Store a decimal value for the paddle's center
        self.center_vert = float(self.image_vert_rec.centery)
        # Movement flag
        self.moving_up = False
        self.moving_down = False

        # Set the dimensions and properties of the horizontal paddles
        self.width_hor = pong_settings.paddle_hor_width
        self.height_hor = pong_settings.paddle_hor_height

        # Built the paddles's rect object
        self.image_hor1_rect = pygame.Rect(0, 0, self.width_hor, self.height_hor)
        # Store a decimal value for the paddle's center
        self.image_hor1_rect.centery = self.screen_rect.bottom - 15
        self.image_hor1_rect.centerx = (pong_settings.screen_width * .25)
        # Properties of the paddle
        self.center_hor1 = float(self.image_hor1_rect.centerx)

        # Built the  second horizontal paddles
        self.image_hor2_rect = pygame.Rect(0, 0, self.width_hor, self.height_hor)
        # Store a decimal value for the paddle's center
        self.image_hor2_rect.centery = self.screen_rect.top + 15
        self.image_hor2_rect.centerx = (pong_settings.screen_width * .25)
        # Store a decimal value for the paddle's center
        self.center_hor2 = float(self.image_hor2_rect.centerx)

    def blit_me(self):
        # Draw a paddle
        pygame.draw.rect(self.screen, self.color, self.image_vert_rec)
        pygame.draw.rect(self.screen, self.color, self.image_hor1_rect)
        pygame.draw.rect(self.screen, self.color, self.image_hor2_rect)

    def center_paddles(self):
        """Center the paddle on the screen"""
        self.center_vert = self.screen_rect.centery
        self.center_hor1 = self.pong_settings.screen_width * .25
        self.center_hor2 = self.pong_settings.screen_width * .25
