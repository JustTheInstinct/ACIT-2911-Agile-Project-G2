import pytest
from models import Sunflower

class maing():
    def __init__(self, money):
        self.money = money
        self.hp = 100
        self.score = 0
        self.remnant_score = 40
        self.difficulty = 1
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