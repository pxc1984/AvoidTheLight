import json

import pygame.font


def load():
    colors = json.load(open('data/gfx/colors.json', 'r'))
    constants = json.load(open('data/constants.json', 'r'))
    return colors, constants


def draw_text(screen, text, text_col, x, y, font):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
