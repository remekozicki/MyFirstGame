import pygame.sprite

from MyFirstGame.Sprites.Bomb import Bomb
from MyFirstGame.Sprites.Tower import Tower


class WeaponMenager(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.towers = []
        self.bombs = pygame.sprite.Group()

    def add_weapon(self, tower_type, pos_x, pos_y):
        if tower_type <= 2:
            self.towers.append(Tower(tower_type, pos_x, pos_y))
        else:
            bomb = Bomb(tower_type, pos_x, pos_y)
            self.bombs.add(bomb)


    def draw_towers(self, screen):
        for tower in self.towers:
            tower.draw(screen)
    def draw_bombs(self, screen):
        for bomb in self.bombs:
            bomb.draw(screen)


    def clear_weapopns(self):
        self.towers = []
        self.bombs = pygame.sprite.Group()

