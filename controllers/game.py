from controllers.base import PygameController
import pygame
import random
from models import Map, Sunflower, PeaShooter, Norzombie, SnowPea, Wallnut, Buckethead, LycheeBomb, Newspaper
from views import MainView
import webbrowser


class GameController(PygameController):
    def __init__(self, username):
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


    def init_plant_points(self):
        for y in range(1, 7):
            points = []
            for x in range(10):
                point = (x, y) # I created a nest loop to mark map position
                points.append(point) # store positions in a list for later use
            self.map_points_list.append(points)

    def init_map(self):
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
            bucketdis = random.randint(3,6) * 100
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
        for e in events:
            if e.type == pygame.QUIT:
                self.endgame()

            elif e.type == pygame.KEYDOWN:

                #trasnfer cordinate to position mark here, 
                x, y = pygame.mouse.get_pos()# // 80
                x = x // 80
                y = y // 80
                #locate which piece of map that plyer mouse clicks 
                gamemap = self.map_list[y - 1][x]
               
                if e.key == pygame.K_1: #create sunflower
                    condition = gamemap.can_grow and self.money >= 50
                    if condition:
                        sunflower = Sunflower(gamemap.position[0], gamemap.position[1], self, self.MainView)
                        self.plants_list.append(sunflower)
                        gamemap.can_grow = False
                        self.money -= 50

                if e.key == pygame.K_2: #create peashooter
                    condition = gamemap.can_grow and self.money >= 50
                    if condition:
                        peashooter = PeaShooter(gamemap.position[0], gamemap.position[1], self, self.MainView)
                        self.plants_list.append(peashooter)
                        gamemap.can_grow = False
                        self.money -= 50
                
                if e.key == pygame.K_3: #create snowpea
                    condition = gamemap.can_grow and self.money >= 60
                    if condition:
                        snowpea = SnowPea(gamemap.position[0], gamemap.position[1], self, self.MainView)
                        self.plants_list.append(snowpea)
                        gamemap.can_grow = False
                        self.money -= 60

                if e.key == pygame.K_4: #create walnut
                    condition = gamemap.can_grow and self.money >= 50
                    if condition:
                        wallnut = Wallnut(gamemap.position[0], gamemap.position[1], self, self.MainView)
                        self.plants_list.append(wallnut)
                        gamemap.can_grow = False
                        self.money -= 50
                
                if e.key == pygame.K_5: #create Lychee Bomb
                    condition = gamemap.can_grow and self.money >= 150
                    if condition:
                        lychee = LycheeBomb(gamemap.position[0], gamemap.position[1], self, self.MainView)
                        self.plants_list.append(lychee)
                        gamemap.can_grow = False
                        self.money -= 150
    
    
    def load_game(self):
        self.init_plant_points()
        self.init_map()
        self.init_zombies()
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
        startimg =  pygame.image.load('./imgs/start.jpg')
        start_game = False
        while (start_game==False):
            self.MainView.window.blit(startimg, (0,0))
            pygame.display.flip()
            for event in pygame.event.get():
                x, y = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 79 < x < 255 and 248 < y < 338:
                        self.GAMEOVER = False # start game
                        self.load_game()
                    elif 282 < x < 400 and 303 < y < 369: # scoreboard
                        webbrowser.open_new("http://127.0.0.1:5000/scoreboard")
                    elif 591 < x < 687 and 337 < y < 372: # about
                        webbrowser.open_new("http://127.0.0.1:5000/about")
                    elif 112 < x < 257 and 348 < y < 413: # Homepage
                        webbrowser.open_new("http://127.0.0.1:5000")
                elif event.type == pygame.QUIT:
                    pygame.quit()



    def aboutus(self):
        pygame.init()
screen=pygame.display.set_mode([800,600])

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

#closing credits or end credits are a list of the movie cast or crew
movie_credits = '''
This video showing how to scroll text
using python coding
has been made by
HAPPY CHUCK PROGRAMMING Channel.
Please support us by clicking Subscribe
Thank you all for watching
'''


centerx, centery = screen.get_rect().centerx, screen.get_rect().centery
deltaY = centery + 50  # adjust so it goes below screen start


running =True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(0)
    deltaY-= 1
    i=0
    msg_list=[]
    pos_list=[]
     
    font = pygame.font.SysFont('Courier', 30)

    #msg = font.render('Hello there, how are you?', True, red)
    for line in movie_credits.split('\n'):
        msg=font.render(line, True, red)
        msg_list.append(msg)
        pos= msg.get_rect(center=(centerx, centery+deltaY+30*i))
        pos_list.append(pos)
        i=i+1
   
    #pos = msg.get_rect(center=(centerx, centery+deltaY))
    

    #if (centery + deltaY < 0):
    #   running = False         # no repetition - once text scrolls up past screen, over 
        
    #screen.blit(msg, pos)
    for j in range(i):
        screen.blit(msg_list[j], pos_list[j])
        
    pygame.display.update()
pygame.quit()

    def endgame(self):
        self.GAMEOVER = True
        endimg =  pygame.image.load('./imgs/gameover.jpg')
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