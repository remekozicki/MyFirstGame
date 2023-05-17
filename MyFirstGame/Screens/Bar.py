import pygame

from MyFirstGame.ImagesPaths import ImagesPaths
from MyFirstGame.Sprites.Button import Button


class Bar:
    def __init__(self, main_game):
        pygame.font.init()

        self.image = pygame.image.load("assets/woodBar.jpg")
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (200, 800))

        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 0

        self.init_buttons()
        self.main_game = main_game

    def init_buttons(self):
        image_paths = ImagesPaths()
        self.weapon_buttons = []

        i = 0
        for path in image_paths.weapons:
            self.weapon_buttons.append(Button(1250, 100 + i * 150, 0.15, path))
            i += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.draw_buttons(screen)
        self.draw_money(screen)

    def draw_buttons(self, screen):
        for button in self.weapon_buttons:
            button.draw(screen)

    def draw_money(self, screen):
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render("gold: " + str(self.main_game.money), False, (255, 255, 255))
        screen.blit(text_surface, (1230, 700))


    def action(self):
        for i, button in enumerate(self.weapon_buttons):
            if button.action():
                self.main_game.set_selected_weapon(i)
                print(i)


