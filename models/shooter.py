from .plant import Plant
import pygame
from pygame import mixer
from .bullet import PeaBullet

class PeaShooter(Plant):
    def __init__(self,x,y, MainGame, MainView):
        super(PeaShooter, self).__init__(MainGame, MainView)

        self.image = pygame.image.load('./imgs/peashooter.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.price = 50
        self.hp = 200
        self.shot_count = 0
        self.should_fire = False

    def shootsound(self):
        self.shoot_sound = mixer.Sound("./sounds/shoop1.wav")
        pygame.mixer.Sound.set_volume(self.shoot_sound, 0.3)
        self.shoot_sound.play()

    def shot(self):
        for zombie in self.MainGame.zombie_list:
            if zombie.rect.y == self.rect.y and zombie.rect.x < 1050 and zombie.rect.x > self.rect.x:
                self.should_fire = True
        if self.live and self.should_fire:
            self.shot_count += 1
            if self.shot_count == 25:
                self.shootsound()
                peabullet = PeaBullet(self, self.MainGame, self.MainView)
                self.MainGame.peabullet_list.append(peabullet)
                self.shot_count = 0

    def display_peashooter(self):
        self.MainView.window.blit(self.image,self.rect)
