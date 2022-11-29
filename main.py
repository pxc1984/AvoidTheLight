import pygame
from data.constants_load import load
import Enemy
import block
import powerup
import Hero
import random

COLORS, CONSTANTS = load()
WIN = pygame.display.set_mode((CONSTANTS['WIDTH'], CONSTANTS['HEIGHT']))
pygame.display.set_caption('Avoid the Light')
WIN.fill(COLORS['background_color'])
clock = pygame.time.Clock()

tiles = [[block.Block(x, y) for x in range(CONSTANTS['WIDTH'] // CONSTANTS['SCALE'])]
         for y in range(CONSTANTS['HEIGHT'] // CONSTANTS['SCALE'])]

print(*[[x.enter() for x in y] for y in tiles], sep='\n')


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    tiles[pygame.mouse.get_pos()[1] // CONSTANTS['SCALE']][
                        pygame.mouse.get_pos()[0] // CONSTANTS['SCALE']].show()
                    print(tiles[pygame.mouse.get_pos()[1] // CONSTANTS['SCALE']][
                        pygame.mouse.get_pos()[0] // CONSTANTS['SCALE']].enter())
                elif event.button == 3:
                    tiles[pygame.mouse.get_pos()[1] // CONSTANTS['SCALE']][
                        pygame.mouse.get_pos()[0] // CONSTANTS['SCALE']].hide()
                elif event.button == 2:
                    for i in tiles:
                        for j in i:
                            j.hide()
                print(pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(CONSTANTS['FPS'])
    pygame.quit()


if __name__ == '__main__':
    main()
