import pygame
from data.useful_functions import load, draw_text
import data.gfx.button
import Enemy
import block
import powerup
import Hero
import random


# TODO: сделай изменение размера пилитки в зависимости от окна (pygame.transform)
def main():
    run = True
    paused = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not paused:
                    tiles[pygame.mouse.get_pos()[1] // CONSTANTS['SCALE']][
                        pygame.mouse.get_pos()[0] // CONSTANTS['SCALE']].show()
                elif event.button == 3 and not paused:
                    tiles[pygame.mouse.get_pos()[1] // CONSTANTS['SCALE']][
                        pygame.mouse.get_pos()[0] // CONSTANTS['SCALE']].hide()
                elif event.button == 2 and not paused:  # DESTRUCTION!!
                    for i in tiles:
                        for j in i:
                            j.hide()
                    draw_text(WIN, 'press SPACE to pause', COLORS['text_color'], 150, 150, font)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if paused:
                        pass
                    elif not paused:
                        if button_resume.draw(WIN):
                            paused = False
                        button_options.draw(WIN)
                        button_quit.draw(WIN)
                    print(paused)
                if event.key == pygame.K_q:
                    WIN.fill((255, 255, 255), (0, 0, 240, 60))

        pygame.display.flip()
        clock.tick(CONSTANTS['FPS'])
    pygame.quit()


if __name__ == '__main__':
    COLORS, CONSTANTS = load()  # Словари с константами
    WIN = pygame.display.set_mode((CONSTANTS['WIDTH'], CONSTANTS['HEIGHT']))  # Основное окно
    pygame.display.set_caption('Avoid the Light')  # Название
    WIN.fill(COLORS['background_color'])  # фон
    # Задание меню паузы
    font = pygame.font.SysFont("arialblack", 30)
    # TODO: сделать отображение фразы чётко по центру с опорой на константы
    draw_text(WIN, 'press SPACE to pause', COLORS['text_color'], 150, 150, font)
    clock = pygame.time.Clock()
    # Тайлы
    tiles = [[block.Block(x, y) for x in range(CONSTANTS['WIDTH'] // CONSTANTS['SCALE'])]
             for y in range(CONSTANTS['HEIGHT'] // CONSTANTS['SCALE'])]
    # Кнопки паузы
    resume_img = pygame.image.load('data/gfx/button_resume.png')
    options_img = pygame.image.load('data/gfx/button_options.png')
    quit_img = pygame.image.load('data/gfx/button_quit.png')
    button_resume = data.gfx.button.Button(225, 34, resume_img, 1)
    button_options = data.gfx.button.Button(217, 150, options_img, 1)
    button_quit = data.gfx.button.Button(256, 266, quit_img, 1)
    main()
