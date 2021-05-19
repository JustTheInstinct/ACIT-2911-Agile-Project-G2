import pygame
class Map():

    def __init__(self, x, y):
        self.position = (x, y)
        self.can_grow = True