from pygame import Rect

class Target:
    """Class to represent a 'target' for the game."""
    def __init__(self, tp_game):
        self.screen = tp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = tp_game.settings

        self.width, self.height = 50, 100
        self.target_color = (0,0,0)

        self.rect = Rect(
            self.screen_rect.right - 70,
            self.screen_rect.top + 10,
            self.width,
            self.height
        )

        self.y = float(self.rect.y)
    
    def update(self):
        """Move target up or down"""
        self.y += self.settings.target_speed * self.settings.target_direction
        self.rect.y = self.y

    def check_edges(self):
        """Return True if the target is at the egde of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.top <= screen_rect.top) or (self.rect.bottom >= screen_rect.bottom)

    def draw_target(self):
        self.screen.fill(self.target_color, self.rect)