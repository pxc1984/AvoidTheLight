import pygame
from data.useful_functions import load
from map import Map as Level

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
        self.rect = pygame.Rect(self.x, self.y, self.x + 64, self.y + 64)
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

    def check_collision(self, level: Level):  # Не функция, а одни проблемы. Зачем я ее вообще написал
        for tile in level.map:
            if self.rect.colliderect(tile.rect):
                return False
            print(self.rect, tile.rect)
        return True

    def move(self, pos):
        self.x += pos[1]
        self.y += pos[0]
        self.rect = pygame.Rect(self.x, self.y, self.x + 64, self.y + 64)

    def draw(self):
        WIN.blit(self.animations['standing'], (self.x, self.y))

    def general_checker(self, amount, direction, level):
        if direction[0] and self.y > 0 and self.check_collision(level):
            self.move((-amount, 0))
        if direction[1] and self.x + 64 < CONSTANTS['WIDTH'] and self.check_collision(level):
            self.move((0, amount))
        if direction[2] and self.y + 64 < CONSTANTS['HEIGHT'] and self.check_collision(level):
            self.move((amount, 0))
        if direction[3] and self.x > 0 and self.check_collision(level):
            self.move((0, -amount))
        self.draw()
