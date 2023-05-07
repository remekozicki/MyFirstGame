import pygame
from ImagesPaths import ImagesPaths


class Map:

    def __init__(self, map_variant):
        self.set_map_attributes(map_variant)

    def set_map_attributes(self, map_variant):
        images_paths = ImagesPaths()

        if map_variant == 0:
            self.image = pygame.image.load(images_paths.maps[0])
            self.path = [(10, 310), (570, 310), (570, 120), (370, 120), (370, 620), (165, 620), (165, 440), (730, 440),
                         (730, 240), (880, 240), (880, 550), (515, 550), (515, 1000)]

        elif map_variant == 1:
            self.image = pygame.image.load(images_paths.maps[1])
            self.path = []

        elif map_variant == 2:
            self.image = pygame.image.load(images_paths.maps[2])
            self.path = []

        elif map_variant == 3:
            self.image = pygame.image.load(images_paths.maps[3])
            self.path = []

        else:
            print("ERRROOOR")

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
