from MyFirstGame.Sprites.Bomb import Bomb
from MyFirstGame.Sprites.Tower import Tower


class WeaponMenager():

    def __init__(self):
        self.towers = []
        self.bombs = []

    def add_weapon(self, tower_type, pos_x, pos_y):
        if tower_type <= 2:
            self.towers.append(Tower(tower_type, pos_x, pos_y))
        else:
            self.bombs.append(Bomb(tower_type, pos_x, pos_y))
        print("len", + len(self.towers))

    def draw_towers(self, screen):
        for tower in self.towers:
            tower.draw(screen)
    def draw_bombs(self, screen):
        for bomb in self.bombs:
            bomb.draw(screen)


    def clear_weapopns(self):
        self.towers = []
        self.bombs = []

