import pygame
from pygame import mixer

class PeaBullet(pygame.sprite.Sprite):
    def __init__(self,peashooter, MainGame, MainView):
        mixer.init()
        self.live = True
        self.image = pygame.image.load('./imgs/peabullet.png')
        self.damage = 50
        self.speed  = 10
        self.rect = self.image.get_rect()
        self.rect.x = peashooter.rect.x + 60
        self.rect.y = peashooter.rect.y + 15
        self.MainGame = MainGame
        self.MainView = MainView

    def hitsound(self):
        self.hit_sound = mixer.Sound("./sounds/splat3.wav")
        pygame.mixer.Sound.set_volume(self.hit_sound, 0.3)
        self.hit_sound.play()
    
    def killsound(self):
        self.kill_sound = mixer.Sound("./sounds/splat.wav")
        pygame.mixer.Sound.set_volume(self.kill_sound, 0.3)
        self.kill_sound.play()

    def move_bullet(self):
        if self.rect.x < 800:
            self.rect.x += self.speed
        else:
            self.live = False

    def hit_zombie(self):
        for zombie in self.MainGame.zombie_list:
            if pygame.sprite.collide_rect(self,zombie):
                self.hitsound()
                self.live = False
                zombie.hp -= self.damage
                if zombie.hp <= 0:
                    self.killsound()
                    zombie.live = False
                    self.nextLevel()

    def nextLevel(self):
        self.MainGame.score += 20 # get 20 score for each zombie killed
        self.MainGame.remnant_score -=20
        for i in range(1,100):
            if self.MainGame.score==100*i and self.MainGame.remnant_score==0:
                    self.MainGame.remnant_score=100*i
                    self.MainGame.level+=1
                    self.MainGame.produce_zombie+=50

    def display_peabullet(self):
        self.MainView.window.blit(self.image,self.rect)