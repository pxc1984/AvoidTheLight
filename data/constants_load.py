import json


def load():
    colors = json.load(open('data/gfx/colors.json', 'r'))
    constants = json.load(open('data/constants.json', 'r'))
    return colors, constants
