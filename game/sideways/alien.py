import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
            "alien.bmp"
        ).convert()

        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.alien_speed
        self.rect.x = self.x