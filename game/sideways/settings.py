class Settings:
    """Store all settings for Sideways Shooter."""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 50, 50)

        # Ship settings
        self.ship_speed = 4
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 4
        self.bullet_width = 15
        self.bullet_height = 4
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 5

        # Speed increase factor
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.alien_speed = 0.5

    def increase_speed(self):
        self.alien_speed *= self.speedup_scale