import pygame
from data.useful_functions import load

pygame.init()

COLORS, CONSTANTS = load()


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('data/gfx/powerup.png'), (CONSTANTS['SCALE'], CONSTANTS['SCALE']))
