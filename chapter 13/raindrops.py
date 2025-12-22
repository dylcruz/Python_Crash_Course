import pygame
from pygame.sprite import Sprite
import sys
import random

class Sky:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Raindrops Falling")
        self.clock = pygame.time.Clock()
        self.raindrops = pygame.sprite.Group()
        self._add_raindrops()

    def run_game(self):
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
        self.screen.fill((0, 179, 255))
        self.raindrops.draw(self.screen)
        pygame.display.flip()

    def _add_raindrops(self):
        for i in range(0, 20):
            new_raindrop = Raindrop(self)
            new_raindrop.rect.x = random.randint(50, self.screen.get_width() - 50)
            new_raindrop.rect.y = random.randint(50, self.screen.get_height() - 50)
            self.raindrops.add(new_raindrop)
    
    def _add_raindrop(self):
        new_raindrop = Raindrop(self)
        new_raindrop.rect.x = random.randint(50, self.screen.get_width() - 50)
        new_raindrop.rect.y = 0
        self.raindrops.add(new_raindrop)

    def _update_raindrops(self):
        self.raindrops.update()
        for raindrop in self.raindrops.copy():
            if raindrop.rect.top >= self.screen.get_height():
                self.raindrops.remove(raindrop)
                self._add_raindrop()

class Raindrop(Sprite):
    def __init__(self, sky):
        super().__init__()
        self.screen = sky.screen

        self.image = pygame.image.load('raindrop.bmp')
        self.rect = self.image.get_rect()
        self.speed = 4
    
    def update(self):
        self.rect.y += self.speed

if __name__ == '__main__':
    sky = Sky()
    sky.run_game()