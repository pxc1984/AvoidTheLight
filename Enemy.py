import pygame
import random
from data.useful_functions import load

pygame.init()
pygame.mixer.init()

COLORS, CONSTANTS = load()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.isCollided = {
            'up': False,
            'down': False,
            'left': False,
            'right': False
        }
        self.rect = self.image.get_rect(x=x, y=y)
        self.x = x
        self.y = y
        self.animations = {
            'standing': pygame.image.load('data/gfx/enemy.png')
        }
        self.image = self.animations['standing']
        self.brightness = 10

    def calculate_movement(self):
        pass
