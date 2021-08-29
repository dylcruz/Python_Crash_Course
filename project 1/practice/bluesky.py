import pygame
import sys
from cloud import Cloud

sky_blue = ((107, 173, 255))

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Blue Sky")
	cloud = Cloud(screen)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(sky_blue)
		cloud.blitme()
		pygame.display.flip()

run_game()