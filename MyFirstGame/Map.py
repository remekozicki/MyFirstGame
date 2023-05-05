import pygame


class Map:


    def __init__(self, map_variant):
        self.set_map_attributes(map_variant)

    def set_map_attributes(self, map_variant):
        if map_variant == 0:
            self.image = pygame.image.load("./assets/MonkeyMeadow_No_UI.webp")
            self.path = [(10, 310), (570, 310), (570, 120), (370, 120), (370, 620), (165, 620), (165, 440), (730, 440),
                         (730, 240), (880, 240), (880, 550), (515, 550), (515, 1000)]
        else:
            print("ERRROOOR")


    def draw(self, screen):
        screen.blit(self.image, (0, 0))
