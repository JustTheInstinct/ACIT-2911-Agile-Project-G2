from .plant import Plant
import pygame

class Sunflower(Plant):
    def __init__(self,x,y, MainGame, MainView):
        super(Sunflower, self).__init__(MainGame, MainView)
        self.image = pygame.image.load('./imgs/sunflower.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 50
        self.hp = 100
        self.time_count = 0

    def produce_money(self):
        self.time_count += 1
        if self.time_count == 25:
            self.MainGame.money += 10
            self.time_count = 0

    def display_sunflower(self):
        self.MainView.window.blit(self.image,self.rect)