import pygame
from ..useful_functions import load

COLORS, CONSTANTS = load()


class Heart(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, state: int):
        super().__init__()
        self.x = x
        self.y = y
        self.animations = {
            'full': pygame.transform.scale(pygame.image.load('data/gfx/heart.png'), (CONSTANTS['SCALE']//2, CONSTANTS['SCALE']//2)),
            'half': pygame.transform.scale(pygame.image.load('data/gfx/half_heart.png'), (CONSTANTS['SCALE']//2, CONSTANTS['SCALE']//2)),
            'empty': pygame.transform.scale(pygame.image.load('data/gfx/empty_heart.png'), (CONSTANTS['SCALE']//2, CONSTANTS['SCALE']//2))
        }
        if state == 0:
            self.image = self.animations['empty']
        elif state == 1:
            self.image = self.animations['half']
        elif state == 2:
            self.image = self.animations['full']
        self.rect = self.image.get_rect(x=x, y=y)

    def update(self, surface: pygame.surface.Surface):
        self.draw(surface)
    
    def set(self, state: int=0):
        if state == 0:
            self.image = self.animations['empty']
        elif state == 1:
            self.image = self.animations['half']
        elif state == 2:
            self.image = self.animations['full']

    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.image, self.rect)
    
    def __repr__(self):
        return f'{self.x}, {self.y}'
#
#
# def draw_health(screen: pygame.surface.Surface, hp: int):
#     for i in range()
