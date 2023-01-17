import pygame
from data.useful_functions import load

pygame.init()

COLORS, CONSTANTS = load()

screen = pygame.display.set_mode((CONSTANTS['WIDTH'], CONSTANTS['HEIGHT']))


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('data/gfx/tile.png'), (CONSTANTS['SCALE'], CONSTANTS['SCALE']))
        self.rect = self.image.get_rect(x=x * CONSTANTS['SCALE'], y=y * CONSTANTS['SCALE'])

    def update(self):
        screen.blit(self.image, self.rect)
