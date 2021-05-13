from .plant import Plant
from .explode import Explode
from .lychee_spike import LycheeSpike
import pygame

class LycheeBomb(Plant):
    def __init__(self,x,y, MainGame, MainView):
        super(LycheeBomb, self).__init__(MainGame, MainView)

        self.image = pygame.image.load('./imgs/lychee_bomb.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 175
        self.hp = 200
        self.frame_timer = 0

    def explode(self):
        # Begins explosion
        should_explode = True
        if self.live and should_explode:
            # Plant lives for 30 frames before exploding
            self.frame_timer += 1
            if self.frame_timer == 27:
                self.image = pygame.image.load('./imgs/explosion.png')
                self.image.get_rect()
                self.rect.x = self.rect.x - 80
                self.rect.y = self.rect.y - 80
            if self.frame_timer == 30:
                # Spawn explosion and spikes
                explosion = Explode(self, self.MainGame, self.MainView)
                spike = LycheeSpike(self, self.MainGame, self.MainView)
                self.rect.x = self.rect.x + 80
                self.rect.y = self.rect.y + 80
                spike_two = LycheeSpike(self, self.MainGame, self.MainView)
                self.rect.x = self.rect.x - 80
                self.rect.y = self.rect.y + 80
                spike_three = LycheeSpike(self, self.MainGame, self.MainView)
                self.MainGame.lycheespike_list.append(spike)
                self.MainGame.explosion_list.append(explosion)
                self.MainGame.lycheespike_list.append(spike_two)
                self.MainGame.lycheespike_list.append(spike_three)
                # Reset planting ability
                a = self.rect.y // 80 - 1
                b = self.rect.x // 80
                map = self.MainGame.map_list[a][b]
                map.can_grow = True
                
                self.live = False

    def display_lychee_bomb(self):
        self.MainView.window.blit(self.image,self.rect)
