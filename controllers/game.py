from controllers.base import PygameController
from models import Map, Sunflower, PeaShooter, Norzombie, SnowPea, Wallnut, Buckethead, LycheeBomb, Newspaper
from views import MainView
import webbrowser, pygame, uuid, random, csv
from pygame import mixer


class GameController(PygameController):
    def __init__(self, username):
        mixer.init()
        self.username = username
        self.id = uuid.uuid1().time_low
        self.difficulty = 1
        self.setup()
        self.MainView = MainView(self)
        self.plant_sound = mixer.Sound("./sounds/plant.wav")
        pygame.mixer.Sound.set_volume(self.plant_sound, 0.1)

    def setup(self):
        """default game settings"""
        self.cord_list = []
        self.grid_list = []
        self.level = 1
        self.score = 0
        self.remnant_score = 100
        self.money = 200
        self.plants_list = []
        self.peabullet_list = []
        self.icebullet_list = []
        self.explosion_list = []
        self.lycheespike_list = []
        self.zombie_list = []
        self.count_zombie = 0
        self.produce_zombie = 500
        self.GAMEOVER  = False
        if self.difficulty == 0:
            self.money = 400
            self.produce_zombie = 600
        elif self.difficulty == 2:
            self.money = 100
            self.produce_zombie = 100

    def init_plant_points(self):
        """Create cordiantion"""
        for y in range(1, 7):
            points = []
            for x in range(13):
                point = (x, y)
                points.append(point)
            self.cord_list.append(points)

    def init_grid(self):
        """Create map list with nest loop"""
        for points in self.cord_list:
            column_grid_list = []
            for point in points:
                    grid = Map(point[0] * 80, point[1] * 80)
                    column_grid_list.append(grid)
            self.grid_list.append(column_grid_list)


    def init_zombies(self):
        """Spawn zombies"""
        time_count = 0
        for i in range(1, 7):
            normaldis = random.randint(1,3) * 200
            normalzombie = Norzombie(1000+ normaldis, i * 80, self, self.MainView)
            bucketdis = random.randint(4,6) * 200
            buckethead = Buckethead(1000 + bucketdis, i * 80, self, self.MainView)
            newsdis = random.randint(3,6) * 100
            newspaper = Newspaper(1000 + newsdis, i * 80, self, self.MainView)
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
        """check user actions in game interface"""
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                self.endgame()

            elif e.type == pygame.KEYDOWN:
                #trasnfer cordinate to position mark here, 
                x, y = pygame.mouse.get_pos()
                if 255 < x < 1000 and 60 < y < 580:
                    x = x // 80
                    y = y // 100
                    #locate which piece of map that plyer mouse clicks 
                    grid = self.grid_list[y - 1][x]
                
                    if e.key == pygame.K_1: #create sunflower
                        condition = grid.can_grow and self.money >= 50
                        if condition:
                            self.plant_sound.play()
                            sunflower = Sunflower(grid.position[0], grid.position[1], self, self.MainView)
                            self.plants_list.append(sunflower)
                            grid.can_grow = False
                            self.money -= 50

                    if e.key == pygame.K_2: #create peashooter
                        condition = grid.can_grow and self.money >= 50
                        if condition:
                            self.plant_sound.play()
                            peashooter = PeaShooter(grid.position[0], grid.position[1], self, self.MainView)
                            self.plants_list.append(peashooter)
                            grid.can_grow = False
                            self.money -= 50
                    
                    if e.key == pygame.K_3: #create snowpea
                        condition = grid.can_grow and self.money >= 60
                        if condition:
                            self.plant_sound.play()
                            snowpea = SnowPea(grid.position[0], grid.position[1], self, self.MainView)
                            self.plants_list.append(snowpea)
                            grid.can_grow = False
                            self.money -= 60

                    if e.key == pygame.K_4: #create walnut
                        condition = grid.can_grow and self.money >= 50
                        if condition:
                            self.plant_sound.play()
                            wallnut = Wallnut(grid.position[0], grid.position[1], self, self.MainView)
                            self.plants_list.append(wallnut)
                            grid.can_grow = False
                            self.money -= 50
                    
                    if e.key == pygame.K_5: #create Lychee Bomb
                        condition = grid.can_grow and self.money >= 150
                        if condition:
                            self.plant_sound.play()
                            lychee = LycheeBomb(grid.position[0], grid.position[1], self, self.MainView)
                            self.plants_list.append(lychee)
                            grid.can_grow = False
                            self.money -= 150
    
    def load_game(self):
        """load game interface, game start"""
        self.window = pygame.display.set_mode([1400, 560])
        self.setup()
        self.init_plant_points()
        self.init_grid()
        self.init_zombies()
        mixer.init()
        mixer.music.load("./sounds/04 Grasswalk.wav")
        mixer.music.play(-1)
        pygame.display.flip()
        while not self.GAMEOVER:
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
        self.endgame()

    def main_menu(self):
        """load game menu and track user actions on main menu"""
        self.MainView.display_menu()
        mixer.init()
        mixer.music.load("./sounds/lobby.wav")
        mixer.music.play(-1)
        waiting = True
        while waiting:
            for event in pygame.event.get():
                x, y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 89 < x < 287 and 267 < y < 362:
                        self.GAMEOVER = False
                        self.load_game()
                    elif 306 < x < 447 and 314 < y < 401: # scoreboard
                        webbrowser.open_new("https://agileproject-pvz.herokuapp.com/scoreboard")
                    elif 648 < x < 757 and 355 < y < 400: # about
                        self.aboutus()
                    elif 117 < x < 287 and 372 < y < 443: # Homepage
                        self.hard_mode()
                    elif 574 < x < 632 and 444 < y < 540:
                        self.help()
                    elif 489 < x < 559 and 444 < y < 540:
                        exit()
                elif event.type == pygame.QUIT:
                    pygame.quit()
    
    def hard_mode(self):
        """alow players change difficulty level of the game"""
        waiting = True
        while waiting:
            self.MainView.display_mode()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 108 < x < 196 and 324 < y < 369:
                        self.difficulty = 0
                        self.MainView.display_mode()
                    elif 320 < x < 478 and 330 < y < 360:
                        self.difficulty = 1
                        self.MainView.display_mode()
                    elif 596 < x < 705 and 330 < y < 360:
                        self.difficulty = 2
                        self.MainView.display_mode()
                elif event.type == pygame.QUIT:
                        waiting = False
                        self.main_menu()

    def help(self):
        """show game instruction"""
        runing = True
        while runing:
            self.MainView.display_help()
            for event in pygame.event.get():
                 if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 531 < x < 687 and 491 < y < 521:
                        runing = False
                        self.main_menu()

    def aboutus(self):
        """show project team members in rolling credits"""
        x = self.MainView.window.get_rect().centerx 
        y = self.MainView.window.get_rect().centery
        startpos  = y + 50
        running =True
        while running:
            self.MainView.display_background()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.main_menu()

            startpos -= 2
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

    def save_score(self):
        """save players score"""
        with open('./webapp/pvzscore.csv', mode='a+') as player_file:
            score = csv.writer(player_file, delimiter=',')
            score.writerow([f'{self.id}', f'{self.username}', f'{self.level}', f'{self.score}'])
            player_file.close()


    def endgame(self):
        """show game over screen and track players actions"""
        self.save_score()
        waiting = True
        self.MainView.display_endscreen()
        while waiting:
            for event in pygame.event.get():
                x, y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 159 < x < 324 and 506 < y < 537:
                        waiting = False # restart
                        self.GAMEOVER  = False
                        self.load_game()
                    elif 447 < x < 618 and 506 < y < 537:
                        waiting = False
                        self.GAMEOVER  = False
                        self.main_menu() # main menu
