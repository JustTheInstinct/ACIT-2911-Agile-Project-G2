import pygame

class Zombie(pygame.sprite.Sprite):
    def __init__(self, MainGame, MainView):
        super(Zombie, self).__init__()
        self.live=True
        self.MainGame = MainGame
        self.MainView = MainView

    def load_image(self):
        if hasattr(self, 'image') and hasattr(self, 'rect'):
            self.MainView.window.blit(self.image, self.rect)
    
