import pytest
from models import Buckethead

class maing():
    def __init__(self, money):
        self.money = money
        self.hp = 100
        self.score = 0
        self.remnant_score = 40
        self.GAMEOVER  = False
mg = maing(0)
new_buckethead = Buckethead(5,1,mg,'mainview')

def test_init_():
    assert new_buckethead.live == True
    assert new_buckethead.hp == 700
    assert new_buckethead.rect.x == 5
    assert new_buckethead.rect.y == 1
    assert new_buckethead.damage == 2
    assert new_buckethead.speed == 1
    assert new_buckethead.stop == False
    assert new_buckethead.head == True

def test_losehead():
    if new_buckethead.hp == 200:
        assert new_buckethead.head == False 
    if new_buckethead.hp == 500:
        assert new_buckethead.head == True

def test_eat_plant():
    new_buckethead.eat_plant(mg)
    assert new_buckethead.stop == False

def test_move_zombie():
    new_buckethead.move_zombie()
    assert new_buckethead.rect.x == 4
    assert new_buckethead.rect.y == 1