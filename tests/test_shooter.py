import pytest
from .shooter import PeaShooter
from .normalzombie import Norzombie

class Mg:
    def __init__(self, money):
        self.money = money
        self.zombie_list = ['Normalzombie']
        self.plants_list = ['Peashooter']
        self.hp = 100




@pytest.fixture
def ps():
    return PeaShooter(0,0, Mg(1000), 'MainView')
def zombie():
    return Norzombie(50,60, Mg(1000), 'MainView')

def test_init(ps):
    assert ps.price == 50
    assert ps.hp == 200
    assert ps.shot_count == 0
    assert ps.rect.x == 20
    assert ps.rect.y == 50
    assert ps.shoul_fire == False

def test_shot(ps):
    if zombie.rect.y == ps.rect.y and zombie.rect.x < 800 and zombie.rect.x > ps.rect.x:
        assert ps.should_fire == True
    if zombie.rect.y != ps.rect.y and zombie.rect.x < 800 and zombie.rect.x > ps.rect.x:
        assert ps.should_fire == False
    if zombie.rect.y != ps.rect.y and zombie.rect.x > 800 and zombie.rect.x > ps.rect.x:
        assert ps.should_fire == False
    if zombie.rect.y != ps.rect.y and zombie.rect.x > 800 and zombie.rect.x > ps.rect.x:
        assert ps.should_fire == False