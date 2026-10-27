import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite):
    """Bullet fired by aliens."""

    def __init__(self, ai_game, alien):
        super().__init__()

        self.screen = ai_game.screen

        self.rect = pygame.Rect(0, 0, 4, 15)
        self.rect.midbottom = alien.rect.midbottom

        self.color = (255, 0, 0)
        self.speed = ai_game.settings.alien_bullet_speed

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            self.rect
        )