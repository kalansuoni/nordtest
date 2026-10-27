import pygame


class Ship:
    """Manage the player's ship."""

    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
            "ship.bmp"
        ).convert()

        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.left = 20
        self.rect.centery = self.screen_rect.centery

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y

    def center_ship(self):
        self.rect.centery = self.screen_rect.centery
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(
            self.image,
            self.rect
        )