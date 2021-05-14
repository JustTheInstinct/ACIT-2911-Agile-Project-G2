import pygame
class Map():

    map_names_list = ['./imgs/map1.jpg', './imgs/map2.jpg']

    def __init__(self, x, y, img_index, MainView):
        self.image = pygame.image.load(Map.map_names_list[img_index])
        self.position = (x, y)
        self.can_grow = True
        self.MainView = MainView

    def load_map(self):
        # grass_img =  pygame.image.load('./imgs/grass.jpg').convert()
        # self.MainView.window.blit(grass_img, (0,80))
        self.MainView.window.blit(self.image,self.position)