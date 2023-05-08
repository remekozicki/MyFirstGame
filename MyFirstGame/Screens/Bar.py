import pygame

from MyFirstGame.MyFirstGame.ImagesPaths import ImagesPaths
from MyFirstGame.MyFirstGame.Sprites.Button import Button


class Bar:
    def __init__(self, main_screen):

        self.image = pygame.image.load("assets/woodBar.jpg")
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (200, 800))

        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 0

        self.init_buttons()
        self.main_screen = main_screen

    def init_buttons(self):
        image_paths = ImagesPaths()
        self.weapon_buttons = []

        i = 0
        for path in image_paths.weapons:
            self.weapon_buttons.append(Button(1250, 100 + i * 150, 0.15, path))
            i += 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.draw_buttons(surface);

    def draw_buttons(self, surface):
        for button in self.weapon_buttons:
            button.draw(surface)

    def action(self):
        for i, button in enumerate(self.weapon_buttons):
            if button.action():
                self.main_screen.set_selected_weapon(i)
                print(i)



