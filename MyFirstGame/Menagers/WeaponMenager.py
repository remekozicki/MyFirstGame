from MyFirstGame.MyFirstGame.Sprites.Tower import Tower


class WeaponMenager():

    def __init__(self):
        self.towers = []
        self.bombs = []

    def add_weapon(self, tower_type, pos_x, pos_y):
            self.towers.append(Tower(tower_type, pos_x, pos_y))

    def draw(self, screen):
        for tower in self.towers:
            tower.draw(screen)


    def clear_weapopns(self):
        self.towers = []
        self.bombs = []

