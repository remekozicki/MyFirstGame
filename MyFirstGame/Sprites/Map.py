import pygame

from MyFirstGame.MyFirstGame.ImagesPaths import ImagesPaths


class Map:

    def __init__(self, map_variant):
        self.set_map_attributes(map_variant)

    def set_map_attributes(self, map_variant):
        images_paths = ImagesPaths()
        # print(map_variant)
        if map_variant == 0:
            self.image = pygame.image.load(images_paths.maps[0])
            self.path = [(10, 310), (570, 310), (570, 120), (370, 120), (370, 620), (165, 620), (165, 440), (730, 440),
                         (730, 240), (880, 240), (880, 550), (515, 550), (515, 1000)]

        elif map_variant == 1:
            self.image = pygame.image.load(images_paths.maps[1])
            self.path = [(10, 660), (820, 660), (835, 655), (845, 630), (850, 615), (855, 600), (860, 0), (730, 440),
                         (730, 240), (880, 240), (880, 550), (515, 550), (515, 1000)]

        elif map_variant == 2:
            self.image = pygame.image.load(images_paths.maps[2])
            self.path = [(10, 310), (300, 310), (570, 120), (370, 120), (370, 620), (165, 620), (165, 440), (730, 440),
                         (730, 240), (880, 240), (880, 550), (515, 550), (515, 1000)]

        else:
            print("ERRROOOR")

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
