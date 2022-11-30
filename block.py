import pygame
from data.useful_functions import load

pygame.init()

COLORS, CONSTANTS = load()

WIN = pygame.display.set_mode((CONSTANTS['WIDTH'], CONSTANTS['HEIGHT']))


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/gfx/tile.png')
        self.axes = {
            'ul': (x * CONSTANTS['SCALE'], y * CONSTANTS['SCALE']),
            'ur': (x * CONSTANTS['SCALE'], (y + 1) * CONSTANTS['SCALE']),
            'dl': (x * CONSTANTS['SCALE'], y * CONSTANTS['SCALE']),
            'dr': ((x + 1) * CONSTANTS['SCALE'], (y + 1) * CONSTANTS['SCALE'])
        }
        self.rect = pygame.Rect(self.axes['ur'],
                                self.axes['dl'])

    def show(self):
        WIN.blit(self.image, self.axes['ul'])

    def hide(self):  # TODO: hiding doesn't work properly
        WIN.fill(COLORS['background_color'], (self.axes['ul'], self.axes['dr']))

    def set_position(self, x, y):
        self.axes = {
            'ul': (x * CONSTANTS['SCALE'], y * CONSTANTS['SCALE']),
            'ur': (x * CONSTANTS['SCALE'], (y + 1) * CONSTANTS['SCALE']),
            'dl': (x * CONSTANTS['SCALE'], y * CONSTANTS['SCALE']),
            'dr': ((x + 1) * CONSTANTS['SCALE'], (y + 1) * CONSTANTS['SCALE'])
        }

    def enter(self):
        return self.axes['ul']
