import pygame
import random
from data.useful_functions import load
import map as Level
import math

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
        self.brightness = 150
        self.move_speed = {  # сделать зависимость от кадров
            'x': 1,
            'y': 1
        }
        self.current_speed = {
            'x': 0,
            'y': 0
        }
        self.path = {
            'active': 0,
            'direction': 0  # stay calm
        }
        self.light = Light(self.rect.center[0], self.rect.center[1], self)

    def update(self, surface: pygame.surface.Surface, level: Level.Map, events: pygame.event.get(), paused):
        keys = pygame.key.get_pressed()
        if not paused:
            self.calculate_movement(keys)
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

    def calculate_movement(self, keys):
        if self.path['active'] == 64:  # нету пути
            self.path['active'] = 0
            self.path['direction'] = random.randint(0, 9)  # direction where to move UNUSED
            self.path['active'] = True
            if self.path['direction'] == 0:  # 0 - none
                self.current_speed['x'], self.current_speed['y'] = 0, 0
            if self.path['direction'] == 1:  # 1 - up left
                self.current_speed['x'], self.current_speed['y'] = 1, -1
            if self.path['direction'] == 2:  # 2 - up
                self.current_speed['x'], self.current_speed['y'] = 0, -1
            if self.path['direction'] == 3:  # 3 - up right
                self.current_speed['x'], self.current_speed['y'] = 1, -1
            if self.path['direction'] == 4:  # 4 - right
                self.current_speed['x'], self.current_speed['y'] = 1, 0
            if self.path['direction'] == 5:  # 5 - down right
                self.current_speed['x'], self.current_speed['y'] = 1, 1
            if self.path['direction'] == 6:  # 6 - down
                self.current_speed['x'], self.current_speed['y'] = 0, 1
            if self.path['direction'] == 7:  # 7 - down left
                self.current_speed['x'], self.current_speed['y'] = -1, 1
            if self.path['direction'] == 8:  # 8 - left
                self.current_speed['x'], self.current_speed['y'] = -1, 0
        elif self.path['active'] < 64:  # есть путь, проверка выполнился ли путь
            self.path['active'] += 1

        # if keys[pygame.K_LEFT]:
        #     self.current_speed['x'] = self.move_speed['x'] * -1  # left
        # if keys[pygame.K_RIGHT]:
        #     self.current_speed['x'] = self.move_speed['x']  # right
        # if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        #     self.current_speed['x'] = 0
        # if keys[pygame.K_UP]:
        #     self.current_speed['y'] = self.move_speed['y'] * -1  # up
        # if keys[pygame.K_DOWN]:
        #     self.current_speed['y'] = self.move_speed['y']  # down
        # if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        #     self.current_speed['y'] = 0

    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.image, self.rect)


class Light(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy: Enemy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((enemy.brightness*2, enemy.brightness*2))
        self.image.fill(COLORS['background_color'])
        pygame.draw.circle(self.image, (255, 255, 255), (enemy.brightness, enemy.brightness), enemy.brightness)
        self.rect = self.image.get_rect(x=x, y=y)

    def update(self, surface: pygame.surface.Surface, enemy: Enemy, level: Level):
        self.draw(surface, enemy)
        self.redraw(surface, level, enemy)

    def draw(self, surface, enemy: Enemy):
        self.rect.center = enemy.rect.center
        surface.blit(self.image, self.rect)

    def redraw(self, surface: pygame.surface.Surface, level: Level, enemy: Enemy):
        collided_tiles = []
        for tile in level.map:
            if pygame.sprite.collide_rect(self, tile):
                collided_points = []
                if self.rect.collidepoint(tile.rect.topright):
                    collided_points.append(tile.rect.topright)
                if self.rect.collidepoint(tile.rect.topleft):
                    collided_points.append(tile.rect.topleft)
                if self.rect.collidepoint(tile.rect.bottomright):
                    collided_points.append(tile.rect.topright)
                if self.rect.collidepoint(tile.rect.bottomleft):
                    collided_points.append(tile.rect.bottomleft)
                collided_tiles.append(collided_points)
        collided_points = []
        for points in collided_tiles:
            exit_value = sorted(points, key=lambda x: round(math.atan2(x[1] - self.rect.centery, x[0] - self.rect.centerx), 4))
            collided_points.append((exit_value[0], exit_value[-1]))  # Нужные точки уже отсортированные
        

    def count_iterable(self, value):
        # interception_with_y, interception_with_x
        try:
            inter_with_x = min((-self.rect.centery*(value[0] - self.rect.centerx)/(value[1] - self.rect.centery)) + self.rect.centerx,
                               (-self.rect.centery*(value[0] - self.rect.centerx)/(value[1]-self.rect.centery)) + self.rect.centerx)
        except ZeroDivisionError:
            return [0, self.rect.centery]
        try:
            inter_with_y = (-self.rect.centerx*(value[1] - self.rect.centery))/(value[1] - self.rect.centerx) + self.rect.centery
        except ZeroDivisionError:
            return [self.rect.centerx, 0]
        if math.sqrt((self.rect.centerx - inter_with_x)**2 + (self.rect.centery)**2) <= math.sqrt((self.rect.centerx)**2 + (self.rect.centery - inter_with_y)**2):
            return [inter_with_x, 0]
        else:
            return [0, inter_with_y]
