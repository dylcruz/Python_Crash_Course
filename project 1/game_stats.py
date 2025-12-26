class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.load_high_score()
        self.reset_stats()
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def load_high_score(self):
        try:
            with open('high_score.txt', 'r', encoding='utf-8') as file:
                self.high_score = int(file.readline())
                file.close()
        except FileNotFoundError:
            self.high_score = 0
