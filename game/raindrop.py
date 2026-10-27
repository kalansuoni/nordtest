import pygame


class Raindrop(pygame.sprite.Sprite):
    """A single raindrop."""

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image = pygame.image.load("raindrop.bmp")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        self.y = float(self.rect.y)

        self.speed = 0.3

    def update(self):
        """Move the raindrop down."""
        self.y += self.speed
        self.rect.y = self.y

    def check_edges(self):
        """Return True if off bottom of screen."""
        screen_rect = self.screen.get_rect()
        return self.rect.top >= screen_rect.bottom