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


# TODO: сделай изменение размера плитки в зависимости от окна (pygame.transform)
def main():
    global fps
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
        if hero.can_play:
            draw_text(WIN, 'press SPACE to pause', COLORS['text_color'], 150, 150, hint_font)  # Текст подсказки
            enemy.update(WIN, level, pygame.event.get(), paused)
            draw_text(WIN, str(hero.update(WIN, level, enemy, pygame.event.get(), paused)),
                      COLORS['background_color'], 560, 20, fps_font)  # Печатает скорость(смотри заметку в Hero)
            level.draw()  # уровень
            draw_text(WIN, str(round(1000 / fps)), COLORS['text_color'], 600, 0, fps_font)  # фпс
        if not hero.can_play:
            game_over()
        draw_pause() if paused else None
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
    hint_font = pygame.font.SysFont("arialblack", 30)  # шрифт подсказок
    fps_font = pygame.font.SysFont("arialblack", 14)
    over_font = pygame.font.SysFont("arialblack", 50)
    clock = pygame.time.Clock()
    # Герой
    hero = Hero.Hero(0, 0)
    enemy = Enemy.Enemy(random.randint(5, 9), random.randint(1, 5))
    # Кнопки паузы
    resume_img = pygame.image.load('data/gfx/button_resume.png')
    options_img = pygame.image.load('data/gfx/button_options.png')
    quit_img = pygame.image.load('data/gfx/button_quit.png')
    button_resume = data.gfx.button.Button(225, 34, resume_img, 1)
    button_options = data.gfx.button.Button(217, 150, options_img, 1)
    button_quit = data.gfx.button.Button(256, 266, quit_img, 1)
    main()
