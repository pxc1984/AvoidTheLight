import pygame


class Button:
    def __init__(self, x, y, image, scale_x, scale_y):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (scale_x, scale_y))
        print(f"scale: {scale_x, scale_y}; width: {width}; height: {height}")
        self.rect = self.image.get_rect(x=x, y=y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
