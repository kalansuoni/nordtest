import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Bullet fired by ship."""

    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.rect = pygame.Rect(
            0,
            0,
            self.settings.bullet_width,
            self.settings.bullet_height
        )

        self.rect.midleft = (
            game.ship.rect.midright
        )

        self.x = float(self.rect.x)

        self.color = (
            self.settings.bullet_color
        )

    def update(self):

        self.x += self.settings.bullet_speed

        self.rect.x = self.x

    def draw_bullet(self):

        pygame.draw.rect(
            self.screen,
            self.color,
            self.rect
        )