import pygame
from pygame.sprite import Sprite
import sys
import random

class Space:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()
        self._add_stars()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        self.screen.fill((0, 0, 0))
        self.stars.draw(self.screen)
        pygame.display.flip()

    def _add_stars(self):
        for i in range(0, 100):
            new_star = Star(self)
            new_star.rect.x = random.randint(50, 750)
            new_star.rect.y = random.randint(50, 750)
            self.stars.add(new_star)

class Star(Sprite):
    def __init__(self, space):
        super().__init__()
        self.screen = space.screen

        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()

if __name__ == '__main__':
    space = Space()
    space.run_game()