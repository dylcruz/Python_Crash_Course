class GameStats:
    """Track statistics for Target Practice"""

    def __init__(self, tp_game):
        self.settings = tp_game.settings
        self.reset_stats()


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.bullets_left = self.settings.bullet_misses_allowed
        self.target_hits = 0