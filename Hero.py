import pygame
from data.useful_functions import load
from map import Map as Level

pygame.init()
pygame.mixer.init()

COLORS, CONSTANTS = load()

WIN = pygame.display.set_mode((CONSTANTS['WIDTH'], CONSTANTS['HEIGHT']))


class Hero(pygame.sprite.Sprite):
    MAX_HP = 10

    # TODO: нашел интересный баг, при движении влево вверх скорость в 1.5 раза больше чем при движении вправо вниз
    # заметка: при целочисленном делении это не работает(и при int() тоже)
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/gfx/main_character.png')
        self.rect = self.image.get_rect(x=x * CONSTANTS['SCALE'], y=y * CONSTANTS['SCALE'])
        self.isCollided = {
            'up': False,
            'down': False,
            'left': False,
            'right': False
        }
        self.move_speed = {
            'x': 288 // CONSTANTS['FPS'],
            'y': 288 // CONSTANTS['FPS']
        }
        self.current_speed = {
            'x': 0,
            'y': 0
        }

    def update(self, surface: pygame.surface.Surface, level, events: pygame.event.get(), paused):
        keys = pygame.key.get_pressed()
        if not paused:
            self.check_controls(keys, events)
            self.rect.y += self.current_speed['y']
            self.checkCollide_y(level)
            self.rect.x += self.current_speed['x']
            self.checkCollide_x(level)
        self.draw(surface)
        return round(self.current_speed['x'], 1), round(self.current_speed['y'], 1)

    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.image, self.rect)

    def check_controls(self, keys, events=None):
        # events можно использовать так как pygame не любит когда много раз вызывают event.get()
        if keys[pygame.K_a]:
            self.current_speed['x'] = self.move_speed['x'] * -1  # left
        if keys[pygame.K_d]:
            self.current_speed['x'] = self.move_speed['x']  # right
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.current_speed['x'] = 0
        if keys[pygame.K_w]:
            self.current_speed['y'] = self.move_speed['y'] * -1  # up
        if keys[pygame.K_s]:
            self.current_speed['y'] = self.move_speed['y']  # down
        if not keys[pygame.K_w] and not keys[pygame.K_s]:
            self.current_speed['y'] = 0

    def checkCollide_x(self, level: Level):
        for tile in level.map:
            if pygame.sprite.collide_rect(self, tile):
                if self.current_speed['x'] > 0:  # right
                    self.rect.right = tile.rect.left
                elif self.current_speed['x'] < 0:  # left
                    self.rect.left = tile.rect.right
        if self.rect.topleft[0] <= 0 and self.current_speed['x'] < 0:  # left
            self.current_speed['x'] = 0
            self.rect.left = 0
        elif self.rect.bottomright[0] >= CONSTANTS['WIDTH'] and self.current_speed['x'] > 0:  # right
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
