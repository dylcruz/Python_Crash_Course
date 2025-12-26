import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()

		# Initialize pygame objects
		self.settings = Settings()
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		
		# Initialize game objects
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self._create_fleet()

		# Start Alien Invasion in an inactive state
		self.game_active = False

		# Initalize all buttons
		self._init_buttons()	

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			
			if self.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()

			self._update_screen()
			self.clock.tick(60)

	def _init_buttons(self):
		sw = self.screen.get_width()
		sh = self.screen.get_height()
		self.buttons = {}

		self.play_button = Button(self, "Play", sw * .4, sh * .4)
		self.buttons[self.play_button] = 'play'
		self.easy_button = Button(self, "Easy", sw * .15, sh * .7)
		self.buttons[self.easy_button] = 'easy'
		self.medium_button = Button(self, "Medium", sw * .40, sh * .7)
		self.buttons[self.medium_button] = 'medium'
		self.hard_button = Button(self, "Hard", sw * .65, sh * .7)
		self.buttons[self.hard_button] = 'hard'

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
				self._check_buttons(mouse_pos)

	def _check_key_down_events(self, event):
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			with open('high_score.txt', 'w', encoding='utf-8') as file:
				file.write(str(self.stats.high_score))
				file.close()
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_p:
			self._start_game()

	def _check_key_up_events(self, event):
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _check_buttons(self, mouse_pos):
		"""Start game or change difficulty settings when buttons are pressed."""
		if self.game_active:
			return
		
		if self.play_button.rect.collidepoint(mouse_pos):
			self._start_game()
			return

		for button, difficulty in self.buttons.items():
			if button.rect.collidepoint(mouse_pos):
				self.settings.set_difficulty(difficulty)
				print(f"Game changed to {difficulty} difficulty")

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.ship.blitme()
		self.aliens.draw(self.screen)
		
		# Draw the score information
		self.sb.show_scoreboard()
		
		# Draw the play and difficulty buttons when game is not active
		if not self.game_active:
			for button in self.buttons.keys():
				button.draw_button()

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

		# Get rid of bullets that have disappeared
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		# Remove any bullets and aliens that have collided.
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True
		)

		if collisions:
			for aliens in collisions.values():
				self.stats.score += self.settings.alien_points * len(aliens)
			self.sb.prep_score()
			self.sb.check_high_score()

		if not self.aliens:
			self._start_new_level()

	def _start_new_level(self):
		self.bullets.empty()
		self._create_fleet()
		self.settings.increase_speed()

		# Increase level.
		self.stats.level += 1
		self.sb.prep_level()

	def _create_alien(self, x_position, y_position):
		"""Creat an alien and place it in the fleet"""
		new_alien = Alien(self)
		new_alien.x = x_position
		new_alien.y = y_position
		new_alien.rect.x = x_position
		new_alien.rect.y = y_position
		self.aliens.add(new_alien)

	def _create_fleet(self):
		"""Create the fleet of aliens"""
		# Create an alien and keep adding aliens until there's no room left.
		# Spacing between aliens is one alien width and one alien height
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size

		current_x, current_y = alien_width, alien_height
		while current_y < (self.settings.screen_height - 3 * alien_height):
			while current_x < (self.settings.screen_width - 2 * alien_width):
				self._create_alien(current_x, current_y)
				current_x += 2 * alien_width
			
			# Finished a row; reset x value, and increment y value
			current_x = alien_width
			current_y += 2 * alien_height

	def _start_game(self):
		# Reset the game statistics
		self.stats.reset_stats()
		self.sb.prep_images()
		self.settings.set_difficulty(self.settings.difficulty)
		self.game_active = True
		
		# Get rid of any remaining bullets and aliens
		self.aliens.empty()
		self.bullets.empty()

		# Create a new fleet and center the ship
		self._create_fleet()
		self.ship.center_ship()

		# Hide the mouse cursor
		pygame.mouse.set_visible(False)

	def _update_aliens(self):
		"""Update the positions of all aliens in the fleet"""
		self._check_fleet_edges()
		self.aliens.update()

		# Look for alien-ship collisions
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		
		self._check_aliens_bottom()

	def _ship_hit(self):
		"""Respond to the ship being hit by an alien."""
		# Decrements ships left.
		if self.stats.ships_left > 0:
			self.stats.ships_left -= 1
			self.sb.prep_ships()

			# Get rid of remaining bullets and aliens
			self.bullets.empty()
			self.aliens.empty()

			# Create a new fleet and center the ship
			self._create_fleet()
			self.ship.center_ship()

			# Pause
			sleep(0.5)
		else:
			self.game_active = False
			pygame.mouse.set_visible(True)

	def _check_aliens_bottom(self):
		"""Check if any aliens have reached the bottom of the screen"""
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= self.settings.screen_height:
				self._ship_hit()
				break

	def _check_fleet_edges(self):
		"""Respond appropriately if any aliens have reached an edge"""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1

if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
