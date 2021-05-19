import pytest
from ..models import Juggernaut

class maing():
    def __init__(self, money):
        self.money = money
        self.hp = 100
        self.score = 0
        self.remnant_score = 40
mg = maing(0)

def test_jug_att():
    new_jug = Juggernaut(5, 1, mg, 'mainview')
    assert new_jug.live == True and new_jug.hp == 10000

def test_jug_eat():
    new_jug = Juggernaut(5,1,mg,'mainview')
    new_jug.eat_plant(mg)
    assert new_jug.stop == False

def test_jug_move():
    new_jug = Juggernaut(1,1,mg,'mainview')
    new_jug.move_zombie()
    assert new_jug.rect.x == 0
    