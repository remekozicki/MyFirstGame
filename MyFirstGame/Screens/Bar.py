import pygame

from MyFirstGame.ImagesPaths import ImagesPaths
from MyFirstGame.Sprites.Bomb import Bomb
from MyFirstGame.Sprites.Button import Button
from MyFirstGame.Sprites.Tower import Tower


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
            if(i < 3):
                self.weapon_buttons.append(Button(1210, 70 + i * 110, 0.20, path))
            else:
                self.weapon_buttons.append(Button(1210, 85 + i * 110, 0.20, path))
            i += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.draw_buttons(screen)
        self.draw_money(screen)
        self.draw_lives(screen)
        self.draw_waves(screen)
        self.draw_prices(screen)
        self.draw_titles(screen)

    def draw_buttons(self, screen):
        for button in self.weapon_buttons:
            # color = (255, 255, 255)
            # pygame.draw.rect(screen, color, pygame.Rect(button.pos_x, button.pos_y, 100, 100))
            button.draw(screen)

    def draw_titles(self,screen):
        my_font = pygame.font.Font('assets/Silkscreen/slkscre.ttf', 25)
        text_tower = my_font.render("TOWERS", False, (255, 255, 255))
        screen.blit(text_tower, (1230, 20))

        text_trap = my_font.render("TRAPS", False, (255, 255, 255))
        screen.blit(text_trap, (1240, 380))


    def draw_prices(self, screen):
        start_group = 85
        for i in range(3):
            my_font = pygame.font.Font('assets/Silkscreen/slkscre.ttf', 10)
            text_price = my_font.render("price: " + str(Tower(i, 0, 0).price), False, (255, 255, 255))
            text_range = my_font.render("range: " + str(Tower(i, 0, 0).range), False, (255, 255, 255))
            text_coldtime = my_font.render("ctime: " + str(Tower(i, 0, 0).coldtime/1000) + "s", False, (255, 255, 255))
            text_demage = my_font.render("attack: " + str(Tower(i, 0, 0).damage), False,(255, 255, 255))

            screen.blit(text_price, (1310, start_group + i * 110))
            screen.blit(text_range, (1310, start_group + i * 110 + 10))
            screen.blit(text_coldtime, (1310, start_group + i * 110 + 20))
            screen.blit(text_demage, (1310, start_group + i * 110 + 30))

        for i in range(3,5):
            my_font = pygame.font.Font('assets/Silkscreen/slkscre.ttf', 10)
            text_surface = my_font.render("price: " + str(Bomb(i, 0, 0).price), False, (255, 255, 255))
            screen.blit(text_surface, (1310, start_group + i * 110 + 15))
            text_surface = my_font.render("range: " + str(Bomb(i, 0, 0).range), False, (255, 255, 255))
            screen.blit(text_surface, (1310, start_group + i * 110 + 25))


    def draw_money(self, screen):
        my_font = pygame.font.Font('assets/Silkscreen/slkscre.ttf', 25)
        text_surface = my_font.render("gold:" + str(self.main_game.money), False, (255, 255, 255))
        screen.blit(text_surface, (1215, 650))

    def draw_lives(self, screen):
        my_font = pygame.font.Font('assets/Silkscreen/slkscre.ttf', 25)
        text_surface = my_font.render("lives:" + str(self.main_game.lives), False, (255, 255, 255))
        screen.blit(text_surface, (1215, 700))

    def draw_waves(self, screen):
        current_wave = self.main_game.wave_menager.wave_index
        all_waves = len(self.main_game.wave_menager.waves)
        my_font = pygame.font.Font('assets/Silkscreen/slkscre.ttf', 25)
        text_surface = my_font.render("wave:" + str(current_wave) + "/" + str(all_waves), False, (255, 255, 255))
        screen.blit(text_surface, (1215, 750))


    def action(self):
        for i, button in enumerate(self.weapon_buttons):
            if button.action():
                self.main_game.set_selected_weapon(i)
                print(i)


