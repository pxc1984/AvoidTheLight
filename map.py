import pygame
import block
from data.useful_functions import load
import random

pygame.init()

COLORS, CONSTANTS = load()

WIN = pygame.display.set_mode((CONSTANTS['WIDTH'], CONSTANTS['HEIGHT']))


class Map:
    def __init__(self, amount: int):
        self.map = []
        self.generate_map(amount)

    def generate_map(self, amount):
        for _ in range(amount):
            self.map.append(block.Block(random.randint(1, 7), random.randint(1, 5)))

    def draw(self):
        for i in self.map:
            i.show()
