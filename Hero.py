import pygame
from data.useful_functions import load

pygame.init()
pygame.mixer.init()

COLORS, CONSTANTS = load()

WIN = pygame.display.set_mode((CONSTANTS['WIDTH'], CONSTANTS['HEIGHT']))


# TODO: Написать обработчик состояния света, обработчик перемещения


class Hero(pygame.sprite.Sprite):
    MAX_HP = 10

    def __init__(self, x, y):
        # TODO: Добавить музыку и звуковые эффекты при ударах и коллизии
        self.can_play = True
        self.hp = Hero.MAX_HP
        self.x = x
        self.y = y
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

    def check_collision(self, direction):  # Не функция, а одни проблемы. Зачем я ее вообще написал
        if self.y > 0 and direction[0]:
            return True
        elif self.x + 64 < CONSTANTS['WIDTH'] and direction[1]:
            return True
        elif self.y + 64 < CONSTANTS['HEIGHT'] and direction[2]:
            return True
        elif self.x > 0 and direction[3]:
            return True
        return False

    def move(self, pos):
        self.x += pos[1]
        self.y += pos[0]

    def draw(self):
        WIN.blit(self.animations['standing'], (self.x, self.y))

    def general_checker(self, amount, direction):
        if direction[0] and self.y > 0:
            self.move((-amount, 0))
        if direction[1] and self.x + 64 < CONSTANTS['WIDTH']:
            self.move((0, amount))
        if direction[2] and self.y + 64 < CONSTANTS['HEIGHT']:
            self.move((amount, 0))
        if direction[3] and self.x > 0:
            self.move((0, -amount))
        self.draw()
