import pygame

class Star:
    """A class to manage a single star."""

    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load("star.bmp")
        self.image.set_colorkey((255, 255, 255))  
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def draw_star(self):
        """Draw the star at its current location."""
        self.screen.blit(self.image, self.rect)