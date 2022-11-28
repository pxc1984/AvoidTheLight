import pygame
import json

with open('data/gfx/colors.json', 'r') as f:
    js = json.load(f)
    BACKGROUND_COLOR = js['background_color']
WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Avoid the Light')
WIN.fill(BACKGROUND_COLOR)



def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
