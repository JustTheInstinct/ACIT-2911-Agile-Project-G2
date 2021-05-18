from models import Sunflower, PeaShooter, SnowPea, Wallnut, LycheeBomb
import pygame

class MainView:
    def __init__(self, MainGame):
        self.MainGame = MainGame


    def init_window(self):
        pygame.display.init()
        pygame.display.set_caption('Plants VS Zombies')
        self.window = pygame.display.set_mode([800, 560])


    def display(self):
        self.display_map()
        self.display_stat()
        self.display_help_text()
        self.display_plants()
        self.display_peabullets()
        self.display_lycheespikes()
        self.display_zombies()
        self.display_icebullets()


    def display_update(self):
        pygame.time.wait(10)
        pygame.display.update()


    def display_stat(self):
        self.window.blit(self.draw_text('Gold$:{}  , Level:{} , Score:{}'.format(self.MainGame.money,self.MainGame.level, self.MainGame.score), 26, (0, 0, 0)), (1000, 40))
        self.window.blit(self.draw_text(
            'You need {} points to reach next level'.format(self.MainGame.remnant_score), 26, (0, 0, 0)), (1000, 60))


    def display_plants(self):
        for plant in self.MainGame.plants_list:
            if plant.live:
                if isinstance(plant, Sunflower):
                    plant.display_sunflower()
                elif isinstance(plant, PeaShooter):
                    plant.display_peashooter()
                elif isinstance(plant, SnowPea):
                    plant.display_snowpea()
                elif isinstance(plant, Wallnut):
                    plant.display_wallnut()
                elif isinstance(plant, LycheeBomb):
                    plant.display_lychee_bomb()

    def display_icebullets(self):
        for i in self.MainGame.icebullet_list:
            if i.live:
                i.display_icebullet()


    def display_peabullets(self):
        for b in self.MainGame.peabullet_list:
            if b.live:
                b.display_peabullet()

    def display_lycheespikes(self):
        for spike in self.MainGame.lycheespike_list:
            if spike.live:
                spike.display_lycheespike()

    def display_zombies(self):
        for zombie in self.MainGame.zombie_list:
            if zombie.live:
                zombie.display_zombie()

    def display_map(self):
        dayimg =  pygame.image.load('./imgs/day.jpeg')
        nightimg = pygame.image.load('./imgs/night.jpg')
        if self.MainGame.difficulty == 2:
            self.window.blit(nightimg,(0,0))
        else:
            self.window.blit(dayimg,(0,0))


    def display_help_text(self):
        text1 = self.draw_text(f'Welcome back {self.MainGame.username}', 60, (255, 0, 0))
        self.window.blit(text1, (1000, 5))

    def display_mode(self):
        diff_img =  pygame.image.load('./imgs/difficulty.jpg')
        self.window.blit(diff_img, (0,0))
        easy = self.draw_text(f'Easy: Less zombie, 400 start gold', 30, (0, 255, 0))
        normal = self.draw_text(f'Normal: More zombie, 200 start gold', 30, (255, 204, 0))
        hard = self.draw_text(f'Easy: Massive zombies and boss Juggernut , 100 start gold', 30, (255, 0, 0))
        self.window.blit(easy, (150, 50))
        self.window.blit(normal, (150, 100))
        self.window.blit(hard, (150, 150))
        if self.MainGame.difficulty == 0:
            mode = "Easy"
        elif self.MainGame.difficulty == 2:
            mode = "Hard"
        else:
            mode = "Normal"
        activated = self.draw_text(f'{mode} mode is activated', 60, (255, 0, 0))
        self.window.blit(activated, (150, 400))
    
    def draw_text(self, content, size, color):
        pygame.font.init()
        font = pygame.font.SysFont('SFNT', size)
        text = font.render(content, True, color)
        return text
    
    def display_menu(self):
        self.window = pygame.display.set_mode([800, 560])
        self.init_window()
        startimg =  pygame.image.load('./imgs/start.jpg')
        self.window.blit(startimg, (0,0))
        pygame.display.flip()
    
    def display_help(self):
        help_img =  pygame.image.load('./imgs/help.png')
        self.window.blit(help_img, (0,0))
        pygame.display.flip()

    def display_background(self):
        backimg = pygame.image.load('./imgs/background.png')
        self.window.blit(backimg, (0,0))

    def display_endscreen(self):
        self.window = pygame.display.set_mode([800, 560])
        end_img = pygame.image.load('./imgs/gameover.jpg')
        self.window.blit(end_img, (0,0))
        pygame.display.flip()