class Settings:
    """A class to stre all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_bullets_allowed = 2

        # Alien settings
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right, -1 represents lefts
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point value increases
        self.score_scale = 1.5

        # Set difficulty to medium by default
        self.difficulty_configs = {
            "easy": {
                "ship_speed": 2,
                "bullet_speed": 3,
                "alien_speed": 0.5,
                "alien_points": 35,
            },
            "medium": {
                "ship_speed": 1.5,
                "bullet_speed": 2.5,
                "alien_speed": 1,
                "alien_points": 50,
            },
            "hard": {
                "ship_speed": 1.5,
                "bullet_speed": 2.5,
                "alien_speed": 1.25,
                "alien_points": 65,
            },
        }

        # Set dynamic settings
        self.difficulty = "medium"
        self.config = self.difficulty_configs[self.difficulty]
        self.ship_speed, self.bullet_speed = 1.5, 2.5
        self.alien_speed, self.alien_points = 1, 50

    def set_difficulty(self, difficulty):
        """Change settings based on difficulty"""
        self.difficulty = difficulty
        self.config = self.difficulty_configs[difficulty]
        for setting, value in self.config.items():
            setattr(self, setting, value)

    def increase_speed(self):
        """Increase the speed settings and alient point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(f"Next level! Aliens are now worth {self.alien_points} points!")
