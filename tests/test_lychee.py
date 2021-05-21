import pytest
from models import LycheeBomb
from models import LycheeSpike

class maing():
    def __init__(self, money):
        self.money = money
        self.hp = 100
        self.score = 0
        self.remnant_score = 40
mg = maing(0)

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
