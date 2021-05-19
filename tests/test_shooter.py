import pytest
from models import PeaShooter, Norzombie
from pygame import mixer



class Mg:
    def __init__(self, money):
        self.money = money
        self.zombie_list = ['Normalzombie']
        self.plants_list = ['Peashooter']
        self.hp = 100

zombie = Norzombie(200,100, Mg(1000), 'MainView')

@pytest.fixture
def ps():
    return PeaShooter(100,100, Mg(1000), 'MainView')

def test_init(ps):
    assert ps.price == 50
    assert ps.hp == 200
    assert ps.shot_count == 0
    assert ps.rect.x == 100
    assert ps.rect.y == 100
    assert ps.should_fire == False

def test_shot(ps):
    if zombie == Norzombie(200,100, Mg(1000), 'MainView'):
        assert ps.should_fire == True
    if zombie == Norzombie(200,200, Mg(1000), 'MainView'):
        assert ps.should_fire == False
    if zombie == Norzombie(50,100, Mg(1000), 'MainView'):
        assert ps.should_fire == False
    if zombie == Norzombie(100,100, Mg(1000), 'MainView'):
        assert ps.should_fire == False
    if zombie == Norzombie(100,200, Mg(1000), 'MainView'):
        assert ps.should_fire == False
    if zombie == Norzombie(50,200, Mg(1000), 'MainView'):
        assert ps.should_fire == False