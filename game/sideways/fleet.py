from random import randint
from alien import Alien


def create_fleet(game):

    game.aliens.empty()

    sample_alien = Alien(game)

    alien_height = sample_alien.rect.height

    rows = 12

    row_spacing = alien_height + 50

    fleet_height = rows * row_spacing

    start_y = (
        game.settings.screen_height - fleet_height
    ) // 2

    for row in range(rows):

        aliens_in_row = randint(1, 2)

        for alien_number in range(aliens_in_row):

            alien = Alien(game)

            alien.rect.x = randint(
                game.settings.screen_width // 2,
                game.settings.screen_width
                - alien.rect.width
            )

            alien.rect.y = (
                start_y
                + row * row_spacing
                + randint(-20, 20)
            )

            alien.x = float(alien.rect.x)

            game.aliens.add(alien)