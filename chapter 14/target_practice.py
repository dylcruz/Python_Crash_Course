import sys

import pygame

from bullet import Bullet
from button import Button
from game_stats import GameStats
from settings import Settings
from ship import Ship
from target import Target

class TargetPractice:
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")
        
        # Initialize objects
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)
        self.play_button = Button(self, "Play")

        # Start Target Practice in an inactive state
        self.game_active = False
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._check_game()
                self._update_target()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_key_down_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()

    def _check_key_up_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.target.draw_target()
        self.ship.blitme()
        
        # Draw the play button if game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # Update bullet positions
        self.bullets.update()

        # Check for bullet and target collisions
        self._check_bullet_target_collisions()
        
        # Get rid of bullets that have missed the target
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
                self.stats.bullets_left -= 1
        
    def _check_bullet_target_collisions(self):
        for bullet in self.bullets:
            if self.target.rect.colliderect(bullet.rect):
                self.bullets.remove(bullet)
                self.stats.target_hits += 1

    def _update_target(self):
        """Updates the targets position"""
        self._check_target_edges()
        self.target.update()

    def _check_target_edges(self):
        if self.target.check_edges():
            self._change_target_direction()

    def _change_target_direction(self):
        self.settings.target_direction *= -1

    def _start_game(self):
        # Reset the game statistics
        self.stats.reset_stats()
        self.settings.initialize_dynamic_settings()
        self.game_active = True
        
        # Set up game
        self.bullets.empty()
        self.ship.center_ship()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

    def _check_game(self):
        if self.stats.target_hits > 2:
            self.stats.reset_stats()
            self.settings.speed_up()
            return
        if self.stats.bullets_left < 1:
            self.game_active = False
            pygame.mouse.set_visible(True)

if __name__ == '__main__':
	# Make a game instance, and run the game.
	tp = TargetPractice()
	tp.run_game()
