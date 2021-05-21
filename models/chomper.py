from models.juggernaut import Juggernaut
from .plant import Plant
import pygame
from pygame import mixer
import time

class Chomper(Plant):
    def __init__(self,x,y, MainGame, MainView):
        super(Chomper, self).__init__(MainGame, MainView)
        mixer.init()
        self.image = pygame.image.load('./imgs/chomper.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 60
        self.hp = 300
        self.can_eat = True
        self.eat_time = 0

    def eatsound(self):
        self.explode_sound = mixer.Sound("./sounds/bite.mp3")
        pygame.mixer.Sound.set_volume(self.explode_sound, 0.3)
        self.explode_sound.play()
    
    def fullsound(self):
        self.explode_sound = mixer.Sound("./sounds/full.mp3")
        pygame.mixer.Sound.set_volume(self.explode_sound, 0.1)
        self.explode_sound.play()

    def eat(self):
        if self.can_eat == False and time.time() - self.eat_time > 10:
                self.reset()
        for zombie in self.MainGame.zombie_list:
            if not isinstance(zombie, Juggernaut) and pygame.sprite.collide_rect(self,zombie) and self.live and self.can_eat:
                self.eatsound()
                self.eat_time = time.time()
                self.image = pygame.image.load('./imgs/eating.png')
                zombie.live = False
                self.can_eat = False
                self.nextLevel()

    def reset(self):
        self.fullsound()
        self.image = pygame.image.load('./imgs/chomper.png')
        self.can_eat = True

    def nextLevel(self):
        self.MainGame.score += 20 # get 20 score for each zombie killed
        self.MainGame.remnant_score -=20
        for i in range(1,100):
            if self.MainGame.score==100*i and self.MainGame.remnant_score==0:
                    self.MainGame.remnant_score=100*i
                    self.MainGame.level+=1
                    self.MainGame.produce_zombie+=50

    def display_chomper(self):
        self.MainView.window.blit(self.image,self.rect)
