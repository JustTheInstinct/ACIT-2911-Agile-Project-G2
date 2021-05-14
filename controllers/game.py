from controllers.base import PygameController
import pygame
from pygame import mixer
import random
from models import Map, Sunflower, PeaShooter, Norzombie, SnowPea, Wallnut, Buckethead, LycheeBomb, Newspaper
from views import MainView
import webbrowser


class GameController(PygameController):
    def __init__(self, username):
        mixer.init()
        self.userName = username
        self.level = 1
        self.score = 0
        self.remnant_score = 100
        self.money = 200
        self.map_points_list = []
        self.map_list = []
        self.plants_list = []
        self.peabullet_list = []
        self.icebullet_list = []
        self.explosion_list = []
        self.lycheespike_list = []
        self.zombie_list = []
        self.count_zombie = 0
        self.produce_zombie = 100
        self.MainView = MainView(self)
        self.GAMEOVER  = False
        self.plant_sound = mixer.Sound("./sounds/plant.wav")
        pygame.mixer.Sound.set_volume(self.plant_sound, 0.1)


    def init_plant_points(self):
        """Create cordiantion"""
        for y in range(1, 7):
            points = []
            for x in range(10):
                point = (x, y)
                points.append(point)
            self.map_points_list.append(points)

    def init_map(self):
        """Create map list with nest loop"""
        for points in self.map_points_list:
            column_map_list = []
            for point in points:
                if (point[0]+point[1]) % 2 == 0: #if its x position + y position is even, i will draw light green
                    gamemap = Map(point[0] * 80, point[1] * 80, 0, self.MainView)
                else: #if its  x position + y position is odd, i will draw dark green here
                    gamemap = Map(point[0] * 80, point[1] * 80, 1, self.MainView)
                column_map_list.append(gamemap)
            self.map_list.append(column_map_list)


    def init_zombies(self):
        """Spawn zombies in random lane and at least 200 away from map, it gives players 
        some time to plant sunflower first, since I only draw a 800*560 pygame interface
        player may not see zombies when it spawns. Once it walks in to my interface,
        player can see it """
        time_count = 0
        for i in range(1, 7):
            normaldis = random.randint(1,3) * 200
            normalzombie = Norzombie(800 + normaldis, i * 80, self, self.MainView)
            bucketdis = random.randint(4,6) * 200
            buckethead = Buckethead(800 + bucketdis, i * 80, self, self.MainView)
            newsdis = random.randint(3,6) * 100
            newspaper = Newspaper(800 + newsdis, i * 80, self, self.MainView)
            news = time_count // 5
            buck = time_count // 10
            if news != 0 or buck != 0 or time_count == 0:
                self.zombie_list.append(normalzombie)
                time_count += 1
            if news == 0:
                self.zombie_list.append(newspaper)
                time_count += 1
            if buck // 10 == 0:
                self.zombie_list.append(buckethead)
                time_count += 2

###-------create part done-------------------------------------

    def load_map(self):
        for temp_map_list in self.map_list:
            for map in temp_map_list:
                map.load_map()


    def load_plants(self):
        """Check plants live then check type, then take action. if it is dead, remove from plant list"""
        for plant in self.plants_list:
            if plant.live:
                if isinstance(plant, Sunflower):
                    plant.produce_money()
                elif isinstance(plant, PeaShooter):
                    plant.shot()
                elif isinstance(plant, SnowPea):
                    plant.shot()
                elif isinstance(plant, LycheeBomb):
                    plant.explode()
                elif isinstance(plant, Wallnut):
                    plant.crack()
            else:
                self.plants_list.remove(plant)

    def load_zombies(self):
        """Check zombie status, then take action, if it is dead, remove from zombies list"""
        for zombie in self.zombie_list:
            if zombie.live:
                if isinstance(zombie, Buckethead):
                    zombie.losehead()
                if isinstance(zombie, Newspaper):
                    zombie.losepaper()
                zombie.move_zombie()
                zombie.hit_plant()
            else:
                self.zombie_list.remove(zombie)

    def load_bullets(self):
        """check bullet status, then take action. if it is dead, remove from bullet list."""
        for b in self.peabullet_list:
            if b.live:
                b.move_bullet()
                b.hit_zombie()
            else:
                self.peabullet_list.remove(b)

        for i in self.icebullet_list:
            if i.live:
                i.move_bullet()
                i.hit_zombie()
            else:
                self.icebullet_list.remove(i)
        
        for spike in self.lycheespike_list:
            if spike.live:
                spike.move_spike()
                spike.hit_zombie()
            else:
                self.lycheespike_list.remove(spike)

    def load_explosions(self):
        """ Checks explosion status and takes action. Since explosion is instant, it is removed quickly """
        for explosion in self.explosion_list:
            if explosion.live:
                explosion.hit_zombie()
            else:
                self.explosion_list.remove(explosion)

    def events_handler(self):
        events = pygame.event.get()
        e_one = None
        for e in events:
            if e.type == pygame.QUIT:
                self.endgame()

            elif e.type == pygame.KEYDOWN:
                #trasnfer cordinate to position mark here, 
                x, y = pygame.mouse.get_pos()
                x = x // 80
                y = y // 80
                #locate which piece of map that plyer mouse clicks 
                gamemap = self.map_list[y - 1][x]
            
                if e.key == pygame.K_1: #create sunflower
                    condition = gamemap.can_grow and self.money >= 50
                    if condition:
                        self.plant_sound.play()
                        sunflower = Sunflower(gamemap.position[0], gamemap.position[1], self, self.MainView)
                        self.plants_list.append(sunflower)
                        gamemap.can_grow = False
                        self.money -= 50

                if e.key == pygame.K_2: #create peashooter
                    condition = gamemap.can_grow and self.money >= 50
                    if condition:
                        self.plant_sound.play()
                        peashooter = PeaShooter(gamemap.position[0], gamemap.position[1], self, self.MainView)
                        self.plants_list.append(peashooter)
                        gamemap.can_grow = False
                        self.money -= 50
                
                if e.key == pygame.K_3: #create snowpea
                    condition = gamemap.can_grow and self.money >= 60
                    if condition:
                        self.plant_sound.play()
                        snowpea = SnowPea(gamemap.position[0], gamemap.position[1], self, self.MainView)
                        self.plants_list.append(snowpea)
                        gamemap.can_grow = False
                        self.money -= 60

                if e.key == pygame.K_4: #create walnut
                    condition = gamemap.can_grow and self.money >= 50
                    if condition:
                        self.plant_sound.play()
                        wallnut = Wallnut(gamemap.position[0], gamemap.position[1], self, self.MainView)
                        self.plants_list.append(wallnut)
                        gamemap.can_grow = False
                        self.money -= 50
                
                if e.key == pygame.K_5: #create Lychee Bomb
                    condition = gamemap.can_grow and self.money >= 150
                    if condition:
                        self.plant_sound.play()
                        lychee = LycheeBomb(gamemap.position[0], gamemap.position[1], self, self.MainView)
                        self.plants_list.append(lychee)
                        gamemap.can_grow = False
                        self.money -= 150
    
    
    def load_game(self):
        self.init_plant_points()
        self.init_map()
        self.init_zombies()
        mixer.init()
        mixer.music.load("./sounds/04 Grasswalk.wav")
        mixer.music.play(-1)
        while not self.GAMEOVER:
            self.load_map()
            self.load_plants()
            self.load_bullets()
            self.load_explosions()
            self.events_handler()
            self.load_zombies()
            self.count_zombie += 1
            if self.count_zombie == self.produce_zombie:
                self.init_zombies()
                self.count_zombie = 0
            self.MainView.display()
            self.MainView.display_update()

    def start_game(self):
        self.MainView.init_window()
        mixer.init()
        mixer.music.load("./sounds/lobby.wav")
        mixer.music.play(-1)
        startimg =  pygame.image.load('./imgs/start.jpg')
        start_game = False
        while (start_game==False):
            self.MainView.window.blit(startimg, (0,0))
            pygame.display.flip()
            for event in pygame.event.get():
                x, y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 89 < x < 287 and 267 < y < 362:
                        self.GAMEOVER = False # start game
                        self.load_game()
                    elif 306 < x < 447 and 314 < y < 401: # scoreboard
                        webbrowser.open_new("http://127.0.0.1:5000/scoreboard")
                    elif 648 < x < 757 and 355 < y < 400: # about
                        self.aboutus()
                    elif 117 < x < 287 and 372 < y < 443: # Homepage
                        webbrowser.open_new("http://127.0.0.1:5000")
                elif event.type == pygame.QUIT:
                    pygame.quit()


    def aboutus(self):
        x = self.MainView.window.get_rect().centerx 
        y = self.MainView.window.get_rect().centery
        startpos  = y + 50
        running =True
        while running:
            backimg =  pygame.image.load('./imgs/background.png')
            self.MainView.window.blit(backimg, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.start_game()

            startpos -= 2 # I thinks this speed is ok, what do you guys think
            i=0
            name_list=[]
            position_list=[]
            
            with open('./About_us.txt') as f:
                lines = f.read().splitlines() 
            for content in lines:
                pygame.font.init()
                font = pygame.font.SysFont("comicsansms", 60)
                name = font.render(content, True, (250, 244, 237))
                name_list.append(name)
                position = name.get_rect(center = (x, y + startpos + 60 * i ))
                position_list.append(position)
                i += 1
    
            for j in range(i):
                self.MainView.window.blit(name_list[j], position_list[j])     
            
            pygame.display.update()


    def endgame(self):
        self.GAMEOVER = True
        endimg = pygame.image.load('./imgs/gameover.jpg')
        self.MainView.window.blit(endimg, (0,0))
        pygame.display.flip()
        pygame.time.wait(2000)




    # def sendGameStat(self):
    #     cur_game_state = GameState(self.userName, self.level, self.score, self.remnant_score, self.money,self.GAMEOVER, datetime.now())
    #     url = "http://localhost:5000/update_game_state"
    #     requests.post(
    #         url,
    #         data=cur_game_state.to_json(),
    #         headers={'Content-Type': 'application/json'}
    #     )
    #     if not self.GAMEOVER:
    #         timer = threading.Timer(1, self.sendGameStat)
    #         timer.start()