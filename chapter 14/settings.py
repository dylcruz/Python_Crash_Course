class Settings:
    """A class to stre all settings for Target Practice."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.bullet_misses_allowed = 3

        # Target settings
        self.target_direction = 1

        self.speed_increase = 1.1

    def initialize_dynamic_settings(self):
        self.target_speed = 3
        self.ship_speed = 1.5

    def speed_up(self):
        self.target_speed *= self.speed_increase
        self.ship_speed *= self.speed_increase