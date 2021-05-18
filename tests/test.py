import pytest
from models import Sunflower
from models import Wallnut
from models import Buckethead
from models import LycheeBomb
from models import LycheeSpike
from models import Newspaper

class maing():
    def __init__(self, money):
        self.money = money
        self.hp = 100
        self.score = 0
        self.remnant_score = 40
mg = maing(0)
def test_sunflower_att():
    new_sf = Sunflower(1,9,mg,'mainview')
    new_sf.hp -= 10
    assert new_sf.hp == 90 and new_sf.time_count == 0 and new_sf.rect.y == 9

def test_money():
    new_sf = Sunflower(1,9,mg,'mainview')
    new_sf.produce_money()
    assert new_sf.time_count == 1

def test_money2():
    new_sf = Sunflower(1,9,mg,'mainview')
    i = 0
    while i < 25:
        new_sf.produce_money()
        i += 1
    assert new_sf.time_count == 0

def test_wallnut():
    new_wal = Wallnut(5,1,mg,'mainview')
    new_wal.hp -= 5
    new_wal.price += 5
    assert new_wal.hp == 495 and new_wal.price == 55 and new_wal.rect.x == 5

def test_bucket_att():
    new_buckethead = Buckethead(5,1,mg,'mainview')
    assert new_buckethead.live == True and new_buckethead.hp == 1000

def test_eat():
    new_buckethead = Buckethead(5,1,mg,'mainview')
    new_buckethead.eat_plant(mg)
    assert new_buckethead.stop == False

def test_move():
    new_buckethead = Buckethead(1,1,mg,'mainview')
    new_buckethead.move_zombie()
    assert new_buckethead.rect.x == 0

def test_bucket_move():
    new_buckethead = Buckethead(1,1,mg,'mainview')
    new_buckethead.move_zombie()
    assert new_buckethead.rect.x == 0
    
def test_spike_att():
    new_bomb=LycheeBomb(1,1,mg,'mainview')
    new_spike = LycheeSpike(new_bomb,mg,'mainView')
    assert new_spike.rect.y == 16 and new_spike.rect.x == 61

def test_move():
    new_bomb=LycheeBomb(1,1,mg,'mainview')
    new_spike = LycheeSpike(new_bomb,mg,'mainView')
    new_spike.move_spike()
    assert new_spike.rect.x == 76

def test_lvl():
    new_bomb=LycheeBomb(1,1,mg,'mainview')
    new_spike = LycheeSpike(new_bomb,mg,'mainView')
    new_spike.nextLevel()
    assert new_spike.MainGame.score == 20 and new_spike.MainGame.remnant_score == 20

def test_bomb_att():
    new_bomb=LycheeBomb(1,5,mg,'mainview')
    assert new_bomb.rect.x == 1 and new_bomb.rect.y == 5

def test_bomb_exp():
    new_bomb=LycheeBomb(1,5,mg,'mainview')
    new_bomb.explode()
    assert new_bomb.frame_timer == 1 

def test_news_att():
    new_paper = Newspaper(1,1,mg,'mainview')
    assert new_paper.hp==600

def test_news_lose():
    new_paper = Newspaper(1,1,mg,'mainview')
    new_paper.hp -= 200
    new_paper.losepaper()
    assert new_paper.speed == 2

def test_news_eat():
    new_paper = Newspaper(1,1,mg,'mainview')
    new_paper.eat_plant(mg)
    assert new_paper.stop == False

def test_news_move():
    new_paper = Newspaper(1,1,mg,'mainview')
    new_paper.move_zombie()
    assert new_paper.rect.x == 0