from .plant import Plant
from .explode import Explode
from .lychee_spike import LycheeSpike
import pygame
from pygame import mixer

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
        

    def explodesound(self):
        mixer.init()
        self.explode_sound = mixer.Sound("./sounds/Explosion+3.wav")
        pygame.mixer.Sound.set_volume(self.explode_sound, 0.3)
        self.explode_sound.play()

    def explode(self):
        should_explode = True
        if self.live and should_explode:
            self.frame_timer += 1
            if self.frame_timer == 27:
                self.image = pygame.image.load('./imgs/explosion.png')
                self.explodesound()
                self.image.get_rect()
                self.rect.x = self.rect.x - 80
                self.rect.y = self.rect.y - 80
            if self.frame_timer == 30:
                explosion = Explode(self, self.MainGame, self.MainView)
                if self.rect.y > 40:
                    spike = LycheeSpike(self, self.MainGame, self.MainView)
                    self.MainGame.lycheespike_list.append(spike)
                self.rect.x = self.rect.x + 80
                self.rect.y = self.rect.y + 80
                spike_two = LycheeSpike(self, self.MainGame, self.MainView)
                self.MainGame.lycheespike_list.append(spike_two)
                if self.rect.y < 480:
                    self.rect.x = self.rect.x - 80
                    self.rect.y = self.rect.y + 80
                    spike_three = LycheeSpike(self, self.MainGame, self.MainView)
                    self.MainGame.lycheespike_list.append(spike_three)
                self.MainGame.explosion_list.append(explosion)
                # Reset planting ability
                self.live = False
            a = self.rect.y // 80 - 1
            b = self.rect.x // 80
            map = self.MainGame.grid_list[a][b]
            map.can_grow = True

    def display_lychee_bomb(self):
        self.MainView.window.blit(self.image,self.rect)
