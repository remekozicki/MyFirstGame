import pygame

# from MyFirstGame.ImagesPaths import ImagesPaths
# from MyFirstGame.Sprites.Button import Button

from MyFirstGame.ImagesPaths import ImagesPaths
from MyFirstGame.Sprites.Button import Button


class LevelsMenu:

    def __init__(self, pos_x, pos_y, width, height, main_game, game):
        self.init_buttons()
        self.image = pygame.image.load("assets/woodBar.jpg").convert()
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.main_game = main_game
        self.game = game

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.draw_buttons(surface)

    def init_buttons(self):
        image_paths = ImagesPaths()
        self.maps_buttons = []
        i = 0
        for path in image_paths.maps:
            self.maps_buttons.append(Button(620, 180 + i * 170, 0.2, path))
            i += 1

    def draw_buttons(self, surface):
        for button in self.maps_buttons:
            button.draw(surface)

    def action(self, main_screen):
        for i, button in enumerate(self.maps_buttons):
            if button.action():
                main_screen.set_selected_map(i)
                self.main_game.set_selected_map(i)
                self.game.set_selected_map(i)

