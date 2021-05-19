import pytest
from models import Newspaper

class maing():
    def __init__(self, money):
        self.money = money
        self.hp = 100
        self.score = 0
        self.remnant_score = 40
mg = maing(0)

def test_news_att():
    new_paper = Newspaper(1,1,mg,'mainview')
    assert new_paper.hp==600

def test_news_lose():
    new_paper = Newspaper(1,1,mg,'mainview')
    new_paper.hp -= 200
    new_paper.losepaper()
    assert new_paper.speed == 2

def test_news_eat():
    new_paper = Newspaper(1,1,mg,'mainview')
    new_paper.eat_plant(mg)
    assert new_paper.stop == False

def test_news_move():
    new_paper = Newspaper(1,1,mg,'mainview')
    new_paper.move_zombie()
    assert new_paper.rect.x == 0
    assert new_paper.MainGame.GAMEOVER == True
