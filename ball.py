import pygame
from pygame.sprite import Sprite
from time import sleep
from random import randint


class Ball(Sprite):

    def __init__(self, pong_settings, screen):
        """Initialize the ball and set its starting position."""
        super(Ball, self).__init__()

        self.screen = screen
        self.pong_settings = pong_settings

        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.center = float(self.rect.centerx)

        self.directionx = 1
        self.directiony = 1

    def center_ball(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        x = randint(-4, 4)
        print(x)
        self.directionx = x
        self.directiony = x
        print("y-----<", self.directionx)
        print("x------>", self.directiony)

    def blit_me(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Convert to degrees
        self.rect.centerx += self.directionx
        self.rect.centery += self.directiony
        sleep(0.0005)
