import pytest
from models import Wallnut

class Mg:
    def __init__(self, money):
        self.money = money
        self.zombie_list = ['Normalzombie']
        self.plants_list = ['Wallnut']
        self.hp = 100

@pytest.fixture
def wl():
    return Wallnut(0,0, Mg(1000), 'MainView')


def test_init(wl):
    assert wl.rect == wl.image.get_rect()
    assert wl.rect.x == 0
    assert wl.rect.y == 0
    assert wl.price == 50
    assert wl.hp == 1000