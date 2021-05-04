from .plant import Plant
import pygame
from .icebullet import IceBullet

class SnowPea(Plant):
    def __init__(self,x,y, MainGame, MainView):
        super(SnowPea, self).__init__(MainGame, MainView)

        self.image = pygame.image.load('./imgs/snowpea.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 60
        self.hp = 200
        self.shot_count = 0


    def shot(self):

        should_fire = False
        for zombie in self.MainGame.zombie_list:
            if zombie.rect.y == self.rect.y and zombie.rect.x < 800 and zombie.rect.x > self.rect.x:
                should_fire = True

        if self.live and should_fire:
            self.shot_count += 1
            if self.shot_count == 25:
                icebullet = IceBullet(self, self.MainGame, self.MainView)
                self.MainGame.icebullet_list.append(icebullet)
                self.shot_count = 0

    
    def display_snowpea(self):
        self.MainView.window.blit(self.image,self.rect)
