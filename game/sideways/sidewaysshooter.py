import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from fleet import create_fleet
from button import Button


class SidewaysShooter:

    def __init__(self):

        pygame.init()

        self.clock = pygame.time.Clock()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width,
                self.settings.screen_height,
            )
        )

        pygame.display.set_caption(
            "Sideways Shooter"
        )

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.score = 0
        self.high_score = 0

        self.lives = self.settings.ship_limit

        self.game_active = False

        self.play_button = Button(
            self,
            "Play"
        )

        create_fleet(self)

    def run_game(self):

        while True:

            self._check_events()

            if self.game_active:

                self.ship.update()

                self._update_bullets()

                self.aliens.update()

                self._check_ship_collisions()

                self._check_left_edge()

            self._update_screen()

            self.clock.tick(60)

    def _start_game(self):

        self.score = 0
        self.lives = self.settings.ship_limit

        self.settings.initialize_dynamic_settings()

        self.bullets.empty()
        self.aliens.empty()

        create_fleet(self)

        self.ship.center_ship()

        self.game_active = True

        pygame.mouse.set_visible(False)

    def _check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    self.ship.moving_up = True

                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True

                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_UP:
                    self.ship.moving_up = False

                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()

                if (
                    not self.game_active
                    and self.play_button.rect.collidepoint(
                        mouse_pos
                    )
                ):
                    self._start_game()

    def _fire_bullet(self):

        if len(self.bullets) < self.settings.bullets_allowed:

            bullet = Bullet(self)

            self.bullets.add(bullet)

    def _update_bullets(self):

        self.bullets.update()

        for bullet in self.bullets.copy():

            if (
                bullet.rect.left >
                self.settings.screen_width
            ):
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):

        collisions = pygame.sprite.groupcollide(
            self.bullets,
            self.aliens,
            True,
            True,
        )

        for aliens_hit in collisions.values():
            self.score += 10 * len(aliens_hit)

        if self.score > self.high_score:
            self.high_score = self.score

        if not self.aliens:

            self.settings.increase_speed()

            create_fleet(self)

    def _check_ship_collisions(self):

        if pygame.sprite.spritecollideany(
            self.ship,
            self.aliens,
        ):
            self._ship_hit()

    def _check_left_edge(self):

        for alien in self.aliens.sprites():

            if alien.rect.left <= 0:

                self._ship_hit()
                break

    def _ship_hit(self):

        self.lives -= 1

        if self.lives <= 0:

            self.game_active = False

            pygame.mouse.set_visible(True)

            return

        self.aliens.empty()
        self.bullets.empty()

        create_fleet(self)

        self.ship.center_ship()

    def _update_screen(self):

        self.screen.fill(
            self.settings.bg_color
        )

        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.set_caption(
            f"Score: {self.score} | "
            f"High Score: {self.high_score} | "
            f"Lives: {self.lives}"
        )

        pygame.display.flip()


if __name__ == "__main__":
    game = SidewaysShooter()
    game.run_game()