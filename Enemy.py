import pygame
import random
from data.useful_functions import load
import map as Level

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
        self.animations = {
            'standing': pygame.image.load('data/gfx/enemy.png')
        }
        self.image = self.animations['standing']
        self.rect = self.image.get_rect(x=x * CONSTANTS['SCALE'], y=y * CONSTANTS['SCALE'])
        self.x = x
        self.y = y
        self.brightness = 10
        self.move_speed = {
            'x': 1,
            'y': 1
        }
        self.current_speed = {
            'x': 0,
            'y': 0
        }

    def update(self, surface: pygame.surface.Surface, level: Level.Map, events: pygame.event.get(), paused):
        keys = pygame.key.get_pressed()
        if not paused:
            self.calculate_movement(events)
            self.rect.y += self.current_speed['y']
            self.checkCollide_y(level)
            self.rect.x += self.current_speed['x']
            self.checkCollide_x(level)
        self.draw(surface)

    def checkCollide_x(self, level: Level):
        for tile in level.map:
            if pygame.sprite.collide_rect(self, tile):
                if self.current_speed['x'] > 0:  # right
                    self.rect.right = tile.rect.left
                elif self.current_speed['x'] < 0:  # left
                    self.rect.left = tile.rect.right
        if self.rect.topleft[0] <= 0 and self.current_speed['x'] < 0:
            self.current_speed['x'] = 0
            self.rect.left = 0
        elif self.rect.bottomright[0] >= CONSTANTS['WIDTH'] and self.current_speed['x'] > 0:
            self.current_speed['x'] = 0
            self.rect.right = CONSTANTS['WIDTH']

    def checkCollide_y(self, level: Level):
        for tile in level.map:
            if pygame.sprite.collide_rect(self, tile):
                if self.current_speed['y'] > 0:  # down
                    self.rect.bottom = tile.rect.top
                elif self.current_speed['y'] < 0:  # up
                    self.rect.top = tile.rect.bottom
        if self.rect.topleft[1] <= 0 and self.current_speed['y'] < 0:  # up
            self.current_speed['y'] = 0
            self.rect.top = 0
        elif self.rect.bottomright[1] >= CONSTANTS['HEIGHT'] and self.current_speed['y'] > 0:  # down
            self.current_speed['y'] = 0
            self.rect.bottom = CONSTANTS['HEIGHT']

    def calculate_movement(self, event=None):
        pos = (random.randint(0, 7), random.randint(0, 5))  # co-ords where to move
        direction = random.randint(0, 3)

    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.image, self.rect)
