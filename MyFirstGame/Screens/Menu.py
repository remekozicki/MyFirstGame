import pygame


class Menu():

    def __init__(self, pos_x, pos_y, width, height):

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = (51, 153, 255)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.pos_x, self.pos_y, self.width, self.height))
