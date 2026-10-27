import pygame


class Target:
    """A moving target."""

    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(
            "target.bmp"
        ).convert()

        self.image.set_colorkey(
            (255, 255, 255)
        )

        self.rect = self.image.get_rect()

        self.screen_rect = (
            self.screen.get_rect()
        )

        self.rect.right = (
            self.screen_rect.right - 20
        )

        self.rect.centery = (
            self.screen_rect.centery
        )

        self.y = float(self.rect.y)

        self.direction = 1

        self.flash_timer = 0

    def update(self):

        self.y += (
            self.settings.target_speed
            * self.direction
        )

        self.rect.y = self.y

        if self.rect.top <= 0:
            self.direction = 1

        if self.rect.bottom >= self.screen_rect.bottom:
            self.direction = -1

        if self.flash_timer > 0:
            self.flash_timer -= 1

    def flash(self):

        self.flash_timer = 60

    def draw(self):

        if self.flash_timer > 0:

            radius = (
                max(
                    self.rect.width,
                    self.rect.height
                ) // 2
            ) + (30 - self.flash_timer)

            pygame.draw.circle(
                self.screen,
                (255, 255, 0),
                self.rect.center,
                radius,
                4
            )

        self.screen.blit(
            self.image,
            self.rect
        )