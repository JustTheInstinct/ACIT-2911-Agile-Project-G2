import pygame

class Explode(pygame.sprite.Sprite):
    def __init__(self,lychee_bomb, MainGame, MainView):
        self.live = True
        self.image = pygame.image.load('./imgs/explosion.png')
        self.damage = 2500
        self.rect = self.image.get_rect()
        self.rect.x = lychee_bomb.rect.x - 80
        self.rect.y = lychee_bomb.rect.y - 80
        self.MainGame = MainGame
        self.MainView = MainView

    def hit_zombie(self):
        for zombie in self.MainGame.zombie_list:
            if pygame.sprite.collide_rect(self,zombie):
                self.live = False
                zombie.hp -= self.damage
                if zombie.hp <= 0:
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


    def display_explosion(self):
        self.MainView.window.blit(self.image,self.rect)