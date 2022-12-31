import pygame
from data.useful_functions import load

pygame.init()

COLORS, CONSTANTS = load()

WIN = pygame.display.set_mode((CONSTANTS['WIDTH'], CONSTANTS['HEIGHT']))


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/gfx/tile.png')
        self.rect = self.image.get_rect(x=x * CONSTANTS['SCALE'], y=y * CONSTANTS['SCALE'])

    def show(self):
        WIN.blit(self.image, self.rect)
        # pygame.draw.rect(WIN, COLORS['background_color'], self.rect)
