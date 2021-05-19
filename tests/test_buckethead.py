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

def test_bucket_att():
    new_buckethead = Buckethead(5,1,mg,'mainview')
    assert new_buckethead.live == True and new_buckethead.hp == 700

def test_eat():
    new_buckethead = Buckethead(5,1,mg,'mainview')
    new_buckethead.eat_plant(mg)
    assert new_buckethead.stop == False

def test_move():
    new_buckethead = Buckethead(1,1,mg,'mainview')
    new_buckethead.move_zombie()
    assert new_buckethead.rect.x == 0