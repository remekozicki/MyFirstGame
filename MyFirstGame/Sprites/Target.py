import math

import pygame

# from MyFirstGame.MyFirstGame.ImagesPaths import ImagesPaths
from MyFirstGame.ImagesPaths import ImagesPaths

class Target(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y, move_path, target_type):
        super().__init__()

        self.target_type = target_type
        self.set_target_attributes(target_type)

        self.path = move_path
        self.path_pos = 0
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = self.path[0][1]

    def set_target_attributes(self, type):
        if type == 0:
            self.image = pygame.image.load(ImagesPaths().enemies[0])
            self.money_per_kill = 5
        elif type == 1:
            self.image = pygame.image.load(ImagesPaths().enemies[1])
            self.money_per_kill = 10
        elif type == 2:
            self.image = pygame.image.load(ImagesPaths().enemies[2])
            self.money_per_kill = 15
        else:
            print("wrong target type")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (520, 2000)
        else:
            x2, y2 = self.path[self.path_pos+1]

        dirn = ((x2-x1)*2, (y2-y1)*2)
        length = math.sqrt((dirn[0])**2 + (dirn[1])**2)
        dirn = (dirn[0]/length, dirn[1]/length)

        self.rect.x += dirn[0] * 5
        self.rect.y += dirn[1] * 5

        # Go to next point
        if dirn[0] >= 0: # moving right
            if dirn[1] >= 0: # moving down
                if self.rect.x >= x2 and self.rect.y >= y2:
                    self.path_pos += 1
            else:
                if self.rect.x >= x2 and self.rect.y <= y2:
                    self.path_pos += 1
        else: # moving left
            if dirn[1] >= 0:  # moving down
                if self.rect.x <= x2 and self.rect.y >= y2:
                    self.path_pos += 1
            else:
                if self.rect.x <= x2 and self.rect.y >= y2:
                    self.path_pos += 1




