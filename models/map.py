import pygame
class Map():

    map_names_list = ['./imgs/map1.png', './imgs/map2.png']

    def __init__(self, x, y, img_index, MainView):
        self.image = pygame.image.load(Map.map_names_list[img_index])
        self.position = (x, y)
        self.can_grow = True
        self.MainView = MainView

    def load_map(self):
        self.MainView.window.blit(self.image,self.position)