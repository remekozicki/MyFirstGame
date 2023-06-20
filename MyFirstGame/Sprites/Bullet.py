import math

import pygame

from MyFirstGame.ImagesPaths import ImagesPaths


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, dest_x, dest_y):
        super().__init__()
        self.x1 = pos_x
        self.y1 = pos_y
        self.x2 = dest_x
        self.y2 = dest_y
        self.image = pygame.image.load("assets/new_bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
        y2 = self.y2

        dirn = ((x2 - x1) * 2, (y2 - y1) * 2)
        length = math.sqrt((dirn[0]) ** 2 + (dirn[1]) ** 2)
        dirn = (dirn[0] / length, dirn[1] / length)

        self.rect.x += dirn[0] * 100
        self.rect.y += dirn[1] * 100



