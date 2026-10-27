class Settings:
    """Settings for Target Practice."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 50, 50)

        # Ship
        self.ship_speed = 0.5

        # Bullet
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 4
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 5

        # Misses before game over
        self.allowed_misses = 3

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.target_speed = 0.2

    def increase_speed(self):
        self.target_speed *= self.speedup_scale