import pygame

class LycheeSpike(pygame.sprite.Sprite):
    def __init__(self, lychee_bomb, MainGame, MainView):
        self.live = True
        self.image = pygame.image.load('./imgs/lychee_spike.png') # Change this
        self.damage = 500
        self.speed  = 15
        self.rect = self.image.get_rect()
        self.rect.x = lychee_bomb.rect.x + 60
        self.rect.y = lychee_bomb.rect.y + 15
        self.MainGame = MainGame
        self.MainView = MainView

    def move_spike(self):
        if self.rect.x < 800:
            self.rect.x += self.speed
        else:
            self.live = False


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



    def display_lycheespike(self):
        self.MainView.window.blit(self.image,self.rect)