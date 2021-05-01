from controllers.base import PygameController
import pygame
import random
from models import Map, Sunflower, PeaShooter, Zombie, GameState, SnowPea, Wallnut
from views import MainView
from datetime import datetime
import threading
import requests

class GameController(PygameController):
    #I set the default money 200, it might be too much, LOL easy game....
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
        self.zombie_list = []
        self.count_zombie = 0
        self.produce_zombie = 100
        self.MainView = MainView(self)
        self.GAMEOVER  = False
        self.sendGameStat()

    def init_plant_points(self):
        #I decide to create a 10 * 7 box,  
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
        for i in range(1, 7):
            dis = random.randint(1, 5) * 200 
            zombie = Zombie(800+ dis, i * 80, self, self.MainView)
            self.zombie_list.append(zombie)

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
            else:
                self.plants_list.remove(plant)

    def load_zombies(self):
        """Check zombie status, then take action, if it is dead, remove from zombies list"""
        for zombie in self.zombie_list:
            if zombie.live:
                zombie.move_zombie()
                zombie.hit_plant()
            else:
                self.zombie_list.remove(zombie)

    def load_peabullets(self):
        """check bullet status, then take action. if it is dead, remove from bullet list."""
        for b in self.peabullet_list:
            if b.live:
                b.move_bullet()
                b.hit_zombie()
            else:
                self.peabullet_list.remove(b)
    
    def load_icebullets(self):
         for i in self.icebullet_list:
            if i.live:
                i.move_bullet()
                i.hit_zombie()
            else:
                self.icebullet_list.remove(i)


    def events_handler(self):
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                self.endgame()
            elif e.type == pygame.MOUSEBUTTONDOWN: 
                #trasnfer cordinate to position mark here, 
                x = e.pos[0] // 80
                y = e.pos[1] // 80
                
                #locate which piece of map that plyer mouse clicks 
                gamemap = self.map_list[y - 1][x]

                condition = gamemap.can_grow and self.money >= 50 # if that square can grow and you have at least 50 gold
                if e.button == 1:   #left button sunflower
                    if condition:
                        sunflower = Sunflower(gamemap.position[0], gamemap.position[1], self, self.MainView)
                        self.plants_list.append(sunflower)
                        gamemap.can_grow = False
                        self.money -= 50
                elif e.button == 3: # right button shooter
                    if condition:
                        peashooter = PeaShooter(gamemap.position[0], gamemap.position[1], self, self.MainView)
                        self.plants_list.append(peashooter)
                        gamemap.can_grow = False
                        self.money -= 50
            elif e.type == pygame.MOUSEWHEEL: 
                if condition:
                    snowpea = SnowPea(gamemap.position[0], gamemap.position[1], self, self.MainView)
                    self.plants_list.append(snowpea)
                    gamemap.can_grow = False
                    self.money -= 70
                        # If number 3 is pressed
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_3:
                    #trasnfer cordinate to position mark here, 
                    x, y = pygame.mouse.get_pos()# // 80
                    x = x // 80
                    y = y // 80
                    #y = e.pos[1] // 80
                    
                    #locate which piece of map that plyer mouse clicks 
                    gamemap = self.map_list[y - 1][x]
                    condition = gamemap.can_grow and self.money >= 100
                    if condition:
                        wallnut = Wallnut(gamemap.position[0], gamemap.position[1], self, self.MainView)
                        self.plants_list.append(wallnut)
                        gamemap.can_grow = False
                        self.money -= 100

    def start_game(self):
        self.MainView.init_window()
        self.init_plant_points()
        self.init_map()
        self.init_zombies()
        while not self.GAMEOVER: # I try to use while loop refresh game, to process objects movement and action
            self.load_map()
            self.load_plants()
            self.load_peabullets()
            self.load_icebullets()
            self.events_handler()
            self.load_zombies()
            self.count_zombie += 1
            if self.count_zombie == self.produce_zombie:
                self.init_zombies()
                self.count_zombie = 0
            self.MainView.display()
            self.MainView.display_update()

    def endgame(self):
        self.MainView.window.blit(self.MainView.draw_text('GAMEOVER', 50, (255, 0, 0)), (300, 200))
        pygame.time.wait(400)
        self.GAMEOVER = True
        self.sendGameStat()


    def sendGameStat(self):
        cur_game_state = GameState(self.userName, self.level, self.score, self.remnant_score, self.money,self.GAMEOVER, datetime.now())
        url = "http://localhost:5000/update_game_state"
        requests.post(
            url,
            data=cur_game_state.to_json(),
            headers={'Content-Type': 'application/json'}
        )
        if not self.GAMEOVER:
            timer = threading.Timer(1, self.sendGameStat)
            timer.start()