import pygame


class Heart:
    def __init__(self, x: int, y: int, state: int):
        self.x = x
        self.y = y
        self.animations = {
            'full': pygame.transform.scale(pygame.image.load('data/gfx/heart.png'), (16, 16)),
            'half': pygame.transform.scale(pygame.image.load('data/gfx/half_heart.png'), (16, 16)),
            'empty': pygame.transform.scale(pygame.image.load('data/gfx/empty_heart.png'), (16, 16))
        }
        if not state:
            self.image = self.animations['empty']
        elif state == 1:
            self.image = self.animations['half']
        elif state == 2:
            self.image = self.animations['full']
        self.rect = self.image.get_rect(x=x, y=y)

    def update(self, surface: pygame.surface.Surface, state: int=0):
        if not state:
            pass
        elif state == 1:
            self.image = self.animations['empty']
        elif state == 1:
            self.image = self.animations['half']
        elif state == 2:
            self.image = self.animations['full']
        self.draw(surface)

    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.image, self.rect)
#
#
# def draw_health(screen: pygame.surface.Surface, hp: int):
#     for i in range()
