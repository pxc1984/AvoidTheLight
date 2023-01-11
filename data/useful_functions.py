import json
import pygame.font


def load():
    colors = json.load(open('data/gfx/colors.json', 'r'))
    constants = json.load(open('data/constants.json', 'r'))
    return colors, constants


def draw_text(screen: pygame.surface.Surface, text: str, text_col: pygame.color, x: int, y: int, font: pygame.font):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
