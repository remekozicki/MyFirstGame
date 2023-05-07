import pygame

from Button import Button
from ImagesPaths import ImagesPaths
from Map import Map


class LevelsMenu:

    def __init__(self, pos_x, pos_y, width, height):
        self.init_buttons()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = (51, 153, 255)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.pos_x, self.pos_y, self.width, self.height))
        self.draw_buttons(surface)

    def init_buttons(self):
        image_paths = ImagesPaths()
        self.maps_buttons = []
        i = 0
        for path in image_paths.maps:
            self.maps_buttons.append(Button(620, 180 + i * 170, 0.2,
                                            path))
            i += 1

    def draw_buttons(self, surface):
        for button in self.maps_buttons:
            button.draw(surface)

    def action(self):
        for i, button in enumerate(self.maps_buttons):
            if button.action():
                # print(i)
                return i
