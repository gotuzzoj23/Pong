from typing import Optional, Any

import pygame.font


class Button:

    msg_image: Optional[Any]

    def __init__(self, pong_settings, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Start screen
        self.bg_width, self.bg_height = pong_settings.screen_width, pong_settings.screen_height
        self.button_color_bg = (255, 255, 255)
        self.text_color_bg = (0, 0, 0)
        self.rect_bg = pygame.Rect(0, 0, self.bg_width, self.bg_height)
        self.rect_bg.center = self.screen_rect.center
        self.font_title = pygame.font.SysFont(None, 500)
        self.font_title_sub = pygame.font.SysFont(None, 20)

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.width_winner, self.height_winner = 500, 100
        self.button_color = (30, 150, 60)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect2 = pygame.Rect(0, 0, self.width_winner, self.height_winner)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery + 200
        self.rect2.centerx = self.screen_rect.centerx
        self.rect2.centery = 200

        # Center divider
        self.width_line, self.height_line = 10, 800
        self.line_color = (255, 255, 255)
        self.line_rect = pygame.Rect(0, 0, self.width_line, self.height_line)
        self.line_rect.centerx = self.screen_rect.centerx

        # The button message needs to be prepped only once
        self.prep_msg(msg)
        self.prep_bg()

    def draw_line(self):
        self.screen.fill(self.line_color, self.line_rect)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the buttom."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()

        self.msg_image_rect.centerx = self.rect.centerx
        self.msg_image_rect.centery = self.rect.centery

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def prep_winner(self, msg2):
        self.msg_image2 = self.font.render(msg2, True, self.text_color, self.button_color)
        self.msg_image_rect2 = self.msg_image2.get_rect()
        self.msg_image_rect2.center = self.rect2.center
        self.screen.fill(self.button_color, self.rect2)
        self.screen.blit(self.msg_image2, self.msg_image_rect2)

    def prep_bg(self):
        self.title = self.font_title.render("PONG", True, self.text_color_bg, self.button_color_bg)
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (self.rect_bg.centerx, 300)

        self.title_sub = self.font_title_sub.render("AI - NO WALLS", True, self.text_color_bg, self.button_color_bg)
        self.title_sub_rect = self.title_sub.get_rect()
        self.title_sub_rect.center = (self.rect_bg.centerx, 450)

    def draw_bg(self):
        self.screen.fill(self.button_color_bg, self.rect_bg)
        self.screen.fill(self.button_color_bg, self.title_rect)
        self.screen.blit(self.title, self.title_rect)

        self.screen.fill(self.button_color_bg, self.title_sub_rect)
        self.screen.blit(self.title_sub, self.title_sub_rect)
