import pygame

class Cloud():
	def __init__(self, screen):
		self.screen = screen

		self.image = pygame.image.load("cloud.bmp")
		self.img_rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.img_rect.centerx = self.screen_rect.centerx
		self.img_rect.centery = self.screen_rect.centery

	def blitme(self):
		self.screen.blit(self.image, self.img_rect)