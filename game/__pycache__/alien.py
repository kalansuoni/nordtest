import pygame


class Alien(pygame.sprite.Sprite):
    """Represents a single alien."""

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load("alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = screen.get_rect().right - self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):
        """Move alien left."""
        self.x -= 1
        self.rect.x = self.x