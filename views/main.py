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
        self.display_stat()
        self.display_help_text()
        self.display_map()
        self.display_plants()
        self.display_peabullets()
        self.display_lycheespikes()
        self.display_zombies()
        self.display_icebullets()


    def display_update(self):
        pygame.time.wait(10)
        pygame.display.update()


    def display_stat(self):
        self.window.fill((255, 255, 255))
        self.window.blit(self.draw_text('GOLD$: {}'.format(self.MainGame.money), 26, (255, 0, 0)), (550, 40))
        self.window.blit(self.draw_text(
            'Level:{}, Score: {}, You still need {} points to reach next level   '.format(self.MainGame.level, self.MainGame.score, self.MainGame.remnant_score), 26, (255, 0, 0)), (5, 40))


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
        for temp_map_list in self.MainGame.map_list:
            for map in temp_map_list:
                map.load_map()


    def display_help_text(self):
        text1 = self.draw_text(f'Welcome back {self.MainGame.username}', 60, (255, 0, 0))
        self.window.blit(text1, (5, 5))


    def draw_text(self, content, size, color):
        pygame.font.init()
        font = pygame.font.SysFont('SFNT', size)
        text = font.render(content, True, color)
        return text