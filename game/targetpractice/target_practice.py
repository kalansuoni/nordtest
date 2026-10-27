import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from target import Target
from game_stats import GameStats
from button import Button


class TargetPractice:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width,
                self.settings.screen_height,
            )
        )

        pygame.display.set_caption(
            "Target Practice"
        )

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

        self.target = Target(self)

        self.stats = GameStats(self)

        self.play_button = Button(
            self,
            "Play"
        )

        self.ding_sound = pygame.mixer.Sound(
            "ding.wav"
        )

        self.ding_sound.set_volume(0.1)

    def run_game(self):

        while True:

            self._check_events()

            if self.stats.game_active:

                self.ship.update()

                self.target.update()

                self.bullets.update()

                self._update_bullets()

            self._update_screen()

    def _check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()

                self._check_play_button(
                    mouse_pos
                )

    def _check_play_button(self, mouse_pos):

        if (
            self.play_button.rect.collidepoint(
                mouse_pos
            )
            and not self.stats.game_active
        ):

            self.settings.initialize_dynamic_settings()

            self.stats.reset_stats()

            self.stats.game_active = True

            self.bullets.empty()

            self.ship.center_ship()

            self.target = Target(self)

            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):

        if event.key == pygame.K_UP:
            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):

        if event.key == pygame.K_UP:
            self.ship.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):

        if len(self.bullets) < self.settings.bullets_allowed:

            bullet = Bullet(self)

            self.bullets.add(bullet)

    def _update_bullets(self):

        for bullet in self.bullets.copy():

            if bullet.rect.left > self.settings.screen_width:

                self.bullets.remove(bullet)

                self.stats.misses += 1

                if (
                    self.stats.misses >=
                    self.settings.allowed_misses
                ):

                    self.stats.game_active = False

                    pygame.mouse.set_visible(
                        True
                    )

        for bullet in self.bullets.copy():

            if self.target.rect.colliderect(
                bullet.rect
            ):

                self.bullets.remove(bullet)

                self.ding_sound.play()

                self.target.flash()

                self.stats.score += 10

                if (
                    self.stats.score >
                    self.stats.high_score
                ):
                    self.stats.high_score = (
                        self.stats.score
                    )

                self.stats.level += 1

                self.settings.increase_speed()

                break

    def _update_screen(self):

        self.screen.fill(
            self.settings.bg_color
        )

        self.ship.blitme()

        self.target.draw()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.set_caption(
            f"Score: {self.stats.score} | "
            f"Level: {self.stats.level} | "
            f"Misses: {self.stats.misses}/"
            f"{self.settings.allowed_misses}"
        )

        pygame.display.flip()


if __name__ == "__main__":

    tp = TargetPractice()

    tp.run_game()