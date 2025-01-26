import pygame
import sys
from pygame.sprite import Sprite

class RocketGame:
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((1000, 1000))
		pygame.display.set_caption("Rocket")
		self.clock = pygame.time.Clock()

		self.rocket = Rocket(self)
		self.bullets = pygame.sprite.Group()

	def run_game(self):
		while True:
			self._check_events()
			self.rocket.update()
			self._update_bullets()
			self._update_screen()
			self.clock.tick(60)


	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				print(event.key)
				self._check_key_down_events(event)
			elif event.type == pygame.KEYUP:
				self._check_key_up_events(event)

	def _check_key_down_events(self, event):
		if event.key == pygame.K_UP:
			self.rocket.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.rocket.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullets()

	def _check_key_up_events(self, event):
		if event.key == pygame.K_UP:
			self.rocket.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.rocket.moving_down = False

	def _update_screen(self):
		self.screen.fill((0, 0, 0))

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		self.rocket.blitme()

		pygame.display.flip()

	def _fire_bullets(self):
		if len(self.bullets) < 3:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		self.bullets.update()

		for bullet in self.bullets.copy():
			if bullet.rect.left > self.screen.get_rect().right:
				self.bullets.remove(bullet)

class Rocket:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)
	
    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 4
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 4
        
class Bullet(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.color = (255, 255, 255)

        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = game.rocket.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        self.x += 8.0
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

if __name__ == '__main__':
    game = RocketGame()
    game.run_game()
