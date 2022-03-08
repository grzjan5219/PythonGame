import pygame
from Game.fruitType import FruitType
from Game.przeszkodaType import PrzeszkodaType

class Field():
    block = None
    color = None
    fruitType = FruitType.none
    przeszkodaType = PrzeszkodaType.none
    przeszkodaDirection = None
    fruit = None
    isFree = True
    def __init__(self):
        pass