import pygame
from data.useful_functions import load, draw_text
import data.gfx.button
import Enemy
import powerup
import Hero
import random
import block
import data.gfx.heart

# I had used this to find, which parts are freezing
import cProfile
import pstats
# <--

# Originally, map was made to play on 16x9 scale
# but not every solution can be used to play
# Tested solutions
#  are those, where width / height is 16 / 9
# Examples are: 1920x1080, 640x360


current_map = 0
maps = [  # map is 16x9
    [  # this is gaming map
        '......-.........',
        '......-......#..',
        '..@.............',
        '......-+........',
        '......--...-----',
        '...........-....',
        '.----......-....',
        '.----...........',
        '+...............',
    ],
    [  # this is a debug map
        '................',
        '.@..............',
        '................',
        '................',
        '................',
        '........-.......',
        '................',
        '..............#.',
        '................',
        '................',
        '................',
    ]
]

def generate_map(temp):
    map = maps[temp]
    for row, line in enumerate(map):
        for column, pos in enumerate(line):
            if pos == '@':  # Hero
                Heroes.add(Hero.Hero(column, row))
            elif pos == '#':  # Enemy
                Enemies.add(Enemy.Enemy(column, row))
            elif pos == '-':  # Tile
                Tiles.add(block.Block(column, row))
            elif pos == '+':  # Powerup
                Powerups.add(powerup.PowerUp(column, row))

def draw_pause():
    '''
    This function draws pause menu over the screen
    '''
    global paused, run
    if button_resume.draw(screen):
        paused = False
    button_options.draw(screen)
    if button_quit.draw(screen):
        run = False


def main():
    global fps, paused, run
    run = True
    # initializing map

    while run:
        events = pygame.event.get()
        keys = pygame.key.get_pressed()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused

        screen.fill(COLORS['background_color'])  # фон
        if Heroes.sprites()[0].can_play:
            Enemies.sprites()[0].light.update(screen, Enemies.sprites()[0], Tiles)  # Light 6
            draw_text(screen, 'press SPACE to pause', COLORS['text_color'], CONSTANTS['WIDTH'] * 0.234, CONSTANTS['HEIGHT'] * 0.39, hint_font)  # Hint 5
        draw_text(screen, str(fps), COLORS['text_color'], CONSTANTS['WIDTH'] * 0.9375, 0, fps_font)  # FPS 5
        if Heroes.sprites()[0].can_play:
            Tiles.update()  # Blocks 4
            Powerups.update() # Powerups
            Enemies.update(fps, screen, Tiles, events, keys, paused)  # Enemy 3
            Heroes.update(fps, screen, Tiles, Enemies, Powerups, events, keys, paused)  # Hero 2
        if not Heroes.sprites()[0].can_play:
            for i in range(1, 4):
                game_over()  # Game Over 2
                Heroes.sprites()[0].kill(screen, i)
                pygame.display.flip()
                clock.tick(1)
                screen.fill(COLORS['background_color'])
            run = False
        update_health(screen, Heroes)
        draw_pause() if paused else None  # Pause 1
        pygame.display.flip()

        fps = round(1000 / clock.tick(CONSTANTS['FPS']))
    pygame.quit()


def game_over():
    '''
    this function shows the GAME OVER menu
    animations on game over must be placed here
    '''
    draw_text(screen, 'GAME OVER', COLORS['game_over'], CONSTANTS['WIDTH'] * 0.23, CONSTANTS['HEIGHT'] * 0.39, over_font)


def update_health(screen, Heroes: pygame.sprite.Group()):
    hp = Heroes.sprites()[0].hp
    hp_list = []
    while hp > 2:
        hp_list.append(2)
        hp -= 2
    if hp % 2 == 1:
        hp_list.append(1)
    elif hp == 0:
        hp_list.append(0)
    elif hp == 2:
        hp_list.append(2)
    while len(hp_list) < 5:
        hp_list.append(0)
    for n, i in enumerate(hp_list):
        Hearts.sprites()[n].set(i)
    Hearts.update(screen)


if __name__ == '__main__':
    COLORS, CONSTANTS = load()  # Словари с константами
    screen = pygame.display.set_mode((CONSTANTS['WIDTH'], CONSTANTS['HEIGHT']))  # Основное окно
    pygame.display.set_caption('Avoid the Light')  # Название
    fps = CONSTANTS['FPS']  # задание фпс для первого кадра

    # Задание меню паузы
    hint_font = pygame.font.SysFont("arialblack", int(CONSTANTS['HEIGHT'] / 12.8))  # шрифт подсказок
    fps_font = pygame.font.SysFont("arialblack", int(CONSTANTS['HEIGHT'] / 27))  # шрифт фпс
    over_font = pygame.font.SysFont("arialblack", int(CONSTANTS['HEIGHT'] / 7.68))  # шрифт доп. вещей

    clock = pygame.time.Clock()

    Tiles = pygame.sprite.Group()
    Heroes = pygame.sprite.Group()
    Enemies = pygame.sprite.Group()
    Powerups = pygame.sprite.Group()

    Hearts = pygame.sprite.Group(*[data.gfx.heart.Heart(i * CONSTANTS['SCALE'] // 2, (CONSTANTS['HEIGHT'] - CONSTANTS['SCALE'] // 2), 2) for i in range(5)])
    generate_map(current_map)

    # Задание кнопок паузы
    resume_img = pygame.image.load('data/gfx/button_resume.png')
    options_img = pygame.image.load('data/gfx/button_options.png')
    quit_img = pygame.image.load('data/gfx/button_quit.png')
    button_resume = data.gfx.button.Button(
        CONSTANTS['WIDTH'] * 0.21, 
        CONSTANTS['HEIGHT'] * 0.12, 
        resume_img, 
        CONSTANTS['WIDTH'] * 0.56, 
        CONSTANTS['HEIGHT'] * 0.18)
    
    button_options = data.gfx.button.Button(
        CONSTANTS['WIDTH'] * 0.21, 
        CONSTANTS['HEIGHT'] * 0.41, 
        options_img, 
        CONSTANTS['WIDTH'] * 0.56, 
        CONSTANTS['HEIGHT'] * 0.18)
    
    button_quit = data.gfx.button.Button(
        CONSTANTS['WIDTH'] * 0.21, 
        CONSTANTS['HEIGHT'] * 0.71, 
        quit_img, 
        CONSTANTS['WIDTH'] * 0.56, 
        CONSTANTS['HEIGHT'] * 0.18)
    
    paused = False
    run = True

    with cProfile.Profile() as pr:  # Это надо чтобы замерить, в каких местах моя программа медленная
        main()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename='needs_prof.prof')
