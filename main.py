import pygame
from data.useful_functions import load, draw_text
import data.gfx.button
import Enemy
# import powerup
import Hero
import random
from map import Map


def draw_pause():
    global paused, run
    if button_resume.draw(WIN):
        paused = False
    button_options.draw(WIN)
    if button_quit.draw(WIN):
        run = False


# TODO: сделай изменение размера плитки в зависимости от окна (pygame.transform)
def main():
    global fps, paused, run
    run = True
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
        if hero.can_play:
            enemy.light.update(WIN, enemy, level)  # Light 6
            draw_text(
                WIN, 'press SPACE to pause',
                COLORS['text_color'],
                CONSTANTS['WIDTH'] * 0.234,
                CONSTANTS['HEIGHT'] * 0.39, 
                hint_font)  # Hint 5
            draw_text(
                WIN, 
                str(round(1000 / fps)), 
                COLORS['text_color'], 
                CONSTANTS['WIDTH'] * 0.9375,
                0, 
                fps_font)  # FPS 5
            level.draw()  # Blocks 4
            enemy.update(
                WIN, 
                level, 
                pygame.event.get(), 
                paused)  # Enemy 3
            hero.update(WIN, level, enemy, pygame.event.get(), paused)  # Hero 2
        if not hero.can_play:
            game_over()  # Game Over 2
        draw_pause() if paused else None  # Pause 1
        pygame.display.flip()
        fps = clock.tick(CONSTANTS['FPS'])
    pygame.quit()


def game_over():
    draw_text(WIN, 'GAME OVER', COLORS['game_over'], 150, 150, over_font)


if __name__ == '__main__':
    COLORS, CONSTANTS = load()  # Словари с константами
    WIN = pygame.display.set_mode((CONSTANTS['WIDTH'], CONSTANTS['HEIGHT']))  # Основное окно
    pygame.display.set_caption('Avoid the Light')  # Название
    fps = CONSTANTS['FPS']  # задание фпс для первого кадра
    # Задание меню паузы
    hint_font = pygame.font.SysFont("arialblack", int(CONSTANTS['HEIGHT'] / 12.8))  # шрифт подсказок
    fps_font = pygame.font.SysFont("arialblack", int(CONSTANTS['HEIGHT'] / 27))  # шрифт фпс
    over_font = pygame.font.SysFont("arialblack", int(CONSTANTS['HEIGHT'] / 7.68))  # шрифт доп. вещей
    clock = pygame.time.Clock()
    # Герой
    hero = Hero.Hero(0, 0)
    enemy = Enemy.Enemy(random.randint(5, 9), random.randint(1, 5))
    # Кнопки паузы
    resume_img = pygame.image.load('data/gfx/button_resume.png')
    options_img = pygame.image.load('data/gfx/button_options.png')
    quit_img = pygame.image.load('data/gfx/button_quit.png')
    button_resume = data.gfx.button.Button(
        CONSTANTS['WIDTH'] * 0.17, 
        CONSTANTS['HEIGHT'] * 0.08, 
        resume_img, 
        CONSTANTS['WIDTH'] * 0.67, 
        CONSTANTS['HEIGHT'] * 0.21)
    button_options = data.gfx.button.Button(
        CONSTANTS['WIDTH'] * 0.17, 
        CONSTANTS['HEIGHT'] * 0.29, 
        options_img, 
        CONSTANTS['WIDTH'] * 0.67, 
        CONSTANTS['HEIGHT'] * 0.21)
    button_quit = data.gfx.button.Button(
        CONSTANTS['WIDTH'] * 0.17, 
        CONSTANTS['HEIGHT'] * 0.58, 
        quit_img, 
        CONSTANTS['WIDTH'] * 0.67, 
        CONSTANTS['HEIGHT'] * 0.21)
    paused = False
    run = True
    main()
