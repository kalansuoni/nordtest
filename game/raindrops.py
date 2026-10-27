import sys
import pygame

from raindrop import Raindrop


def create_raindrop(screen, raindrops, x_position, y_position):
    """Create and place a raindrop."""
    raindrop = Raindrop(screen)
    raindrop.rect.x = x_position
    raindrop.rect.y = y_position
    raindrop.y = float(y_position)
    raindrops.add(raindrop)


def create_rain(screen, raindrops):
    """Create a grid of raindrops."""
    sample_drop = Raindrop(screen)

    drop_width = sample_drop.rect.width
    drop_height = sample_drop.rect.height

    current_y = 0

    while current_y < 800:
        current_x = 0

        while current_x < 1200:
            create_raindrop(
                screen,
                raindrops,
                current_x,
                current_y
            )
            current_x += drop_width * 2

        current_y += drop_height * 2


pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Steady Rain")

raindrops = pygame.sprite.Group()
create_rain(screen, raindrops)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    raindrops.update()

    # Move drops back to the top when they leave the screen
    for raindrop in raindrops.sprites():
        if raindrop.check_edges():
            raindrop.rect.bottom = 0
            raindrop.y = float(raindrop.rect.y)

    screen.fill((25, 25, 25))

    raindrops.draw(screen)

    pygame.display.flip()
