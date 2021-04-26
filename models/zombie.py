import pygame
import time


class Zombie(pygame.sprite.Sprite):
    """Each Zombie 1000HP """
    def __init__(self,x,y, MainGame, MainView):
        super(Zombie, self).__init__()
        self.image = pygame.image.load('./imgs/zombie.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 1000
        self.damage = 2
        self.speed = 1
        self.live = True
        self.stop = False
        self.MainGame = MainGame
        self.MainView = MainView

    def move_zombie(self):
        if self.live and not self.stop:
            self.rect.x -= self.speed
            if self.rect.x < -80:
                self.MainGame.endgame()

    def hit_plant(self):
        for plant in self.MainGame.plants_list:
            if pygame.sprite.collide_rect(self,plant):
                self.stop = True
                self.eat_plant(plant)

    def eat_plant(self,plant):
        plant.hp -= self.damage
        if plant.hp <= 0:
            a = plant.rect.y // 80 - 1
            b = plant.rect.x // 80
            map = self.MainGame.map_list[a][b]
            map.can_grow = True
            plant.live = False
            self.stop = False

    def display_zombie(self):
        self.MainView.window.blit(self.image, self.rect)
