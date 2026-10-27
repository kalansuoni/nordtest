class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 50, 50)

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 128, 0)

        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.alien_bullet_speed = 4

        # Default difficulty
        self.set_medium()

    def set_easy(self):
        self.ship_limit = 5
        self.bullets_allowed = 6

        self.ship_speed = 4
        self.bullet_speed = 5
        self.alien_speed = 1

        self.fleet_drop_speed = 5

        self.alien_points = 50

    def set_medium(self):
        self.ship_limit = 3
        self.bullets_allowed = 5

        self.ship_speed = 6
        self.bullet_speed = 7
        self.alien_speed = 2

        self.fleet_drop_speed = 10

        self.alien_points = 50

    def set_hard(self):
        self.ship_limit = 2
        self.bullets_allowed = 4

        self.ship_speed = 8
        self.bullet_speed = 9
        self.alien_speed = 3

        self.fleet_drop_speed = 15

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(
            self.alien_points * self.score_scale
        )