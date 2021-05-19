import pytest
from models import SnowPea, Norzombie

class maing():
    def __init__(self, money):
        self.money = money
        self.hp = 100
        self.score = 0
        self.remnant_score = 40
        self.GAMEOVER  = False
mg = maing(0)

zombie = Norzombie(200,100, mg, 'MainView')

def test_snow_att():
    new_snow = SnowPea(5,1,mg,'mainview')
    assert new_snow.hp == 200
    assert new_snow.price == 60
    assert new_snow.shot_count == 0
    assert new_snow.rect.x == 5
    assert new_snow.rect.y == 1

def test_shot():
    new_snow = SnowPea(5,1,mg,'mainview')
    if zombie == Norzombie(10,1, mg, 'MainView'):
        assert new_snow.should_fire == True
    if zombie == Norzombie(10,5, mg, 'MainView'):
        assert new_snow.should_fire == False
    if zombie == Norzombie(1,1, mg, 'MainView'):
        assert new_snow.should_fire == False
