import pygame
from data.useful_functions import load, draw_text
import data.gfx.button
import Enemy
import powerup
import Hero
import random
from map import Map


def draw_pause():
    if button_resume.draw(WIN):
        paused = False
    button_options.draw(WIN)
    button_quit.draw(WIN)


# TODO: сделай изменение размера пилитки в зависимости от окна (pygame.transform)
def main():
    run = True
    paused = False
    direction = [0, 0, 0, 0]  # up right down left
    # initializing map
    level = Map(5)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused


        WIN.fill(COLORS['background_color'])  # фон
        # TODO: сделать отображение фразы чётко по центру с опорой на константы
        level.draw()
        if paused:
            hero.update(WIN, level, pygame.event.get(), paused)
            draw_pause()
        else:
            draw_text(WIN, 'press SPACE to pause', COLORS['text_color'], 150, 150, font)
            hero.update(WIN, level, pygame.event.get(), paused)
        pygame.display.flip()
        clock.tick(CONSTANTS['FPS'])
    pygame.quit()


if __name__ == '__main__':
    COLORS, CONSTANTS = load()  # Словари с константами
    WIN = pygame.display.set_mode((CONSTANTS['WIDTH'], CONSTANTS['HEIGHT']))  # Основное окно
    pygame.display.set_caption('Avoid the Light')  # Название
    # Задание меню паузы
    font = pygame.font.SysFont("arialblack", 30)
    clock = pygame.time.Clock()
    # Герой
    hero = Hero.Hero(0, 0)
    # Кнопки паузы
    resume_img = pygame.image.load('data/gfx/button_resume.png')
    options_img = pygame.image.load('data/gfx/button_options.png')
    quit_img = pygame.image.load('data/gfx/button_quit.png')
    button_resume = data.gfx.button.Button(225, 34, resume_img, 1)
    button_options = data.gfx.button.Button(217, 150, options_img, 1)
    button_quit = data.gfx.button.Button(256, 266, quit_img, 1)
    main()
