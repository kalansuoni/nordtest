class GameStats:
    """Track game statistics."""

    def __init__(self, game):
        self.settings = game.settings

        self.reset_stats()

        self.high_score = 0
        self.game_active = False

    def reset_stats(self):
        self.score = 0
        self.level = 1

        self.misses = 0
        self.misses_left = self.settings.allowed_misses