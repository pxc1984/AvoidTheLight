import pygame
from data.useful_functions import load

pygame.init()
pygame.mixer.init()

COLORS, CONSTANTS = load()

# TODO: Написать обработчик состояния света, обработчик перемещения


class Hero(pygame.sprite.Sprite):
    MAX_HP = 10

    def __init__(self, x, y):
        # TODO: Добавить музыку и звуковые эффекты при ударах и коллизии
        self.can_play = True
        self.hp = Hero.MAX_HP
        self.animations = {
            'standing': pygame.image.load('data/gfx/main_character.png')
        }
        pygame.sprite.Sprite.__init__(self)
        self.image = self.animations['standing']
        self.rect = self.image.get_rect(x=x, y=y)
        self.isCollided = {
            'up': False,
            'down': False,
            'left': False,
            'right': False
        }
        self.immortalTime = {
            'max': CONSTANTS['FPS'],
            'current': 0
        }
