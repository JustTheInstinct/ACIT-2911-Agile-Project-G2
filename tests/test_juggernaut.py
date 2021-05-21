import pytest
from models import Juggernaut, Sunflower

class maing():
    def __init__(self, money):
        self.money = money
        self.hp = 100
        self.score = 0
        self.remnant_score = 40
        self.GAMEOVER  = False
        self.difficulty = 2

mg = maing(0)
new_jug = Juggernaut(5, 1, mg, 'mainview')
plant = Sunflower(5,1,mg,'mainview')

def test_jug_att():
    assert new_jug.live == True and new_jug.hp == 5000

def test_jug_move():
    new_jug.move_zombie()
    assert new_jug.rect.x == 4
    assert new_jug.rect.y == 1
    