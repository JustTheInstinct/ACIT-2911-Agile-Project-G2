from .plant import Plant
import pygame

class Wallnut(Plant):
    def __init__(self,x,y, MainGame, MainView):
        super(Wallnut, self).__init__(MainGame, MainView)

        self.image = pygame.image.load('./imgs/wallnut.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 50
        self.hp = 1000

    def display_wallnut(self):
        self.MainView.window.blit(self.image,self.rect)

    def crack(self):
        if self.hp == 500:
            self.image = pygame.image.load('./imgs/cracked.png')
        if self.hp == 300:
            self.image = pygame.image.load('./imgs/broken.png')