import time

import pygame
import random
import sys
from Crosshair import Crosshair
from Bar import Bar
# from MainGame import MainGame
from Target import Target
from Button import Button
from Menu import Menu
from Map import Map
from WeaponMenager import WeaponMenager
from ImagesPaths import ImagesPaths


class GameState():

    def __init__(self):
        self.state = 'intro'
        self.map = Map(0);
        self.weapon_menager = WeaponMenager()

        #TEST
        self.weapon_menager.add_weapon(0, 100, 500);
        self.weapon_menager.add_weapon(1, 300, 500);
        self.weapon_menager.add_weapon(2, 500, 500);
        # test

        self.bar = Bar(self)
        self.selected_weapon = -1;

        # self.main_game_test = MainGame()

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()
        if self.state == 'levels':
            self.select_level()

    def intro(self):
        pygame.mouse.set_visible(True)

        # buttons
        play_button = Button(screen_w / 2 - 75, screen_h / 2 - 150, 0.5,
                             "./assets/orange button/Play orange button 300x80.png")
        quit_button = Button(screen_w / 2 - 75, screen_h / 2 + 100, 0.5,
                             "./assets/orange button/Quit orange button 300x80.png")
        level_button = Button(screen_w / 2 - 75, screen_h / 2, 0.5,
                              "./assets/orange button/level select orange button 300x80.png")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.action():
                    print('quit')
                    pygame.quit()
                    sys.exit()

                if play_button.action():
                    print("play")
                    for i in range(20):
                        newT = Target("./assets/new_bullet.png", -random.randrange(0, 100) * 5, 0, self.map.path)
                        targetGroup.add(newT)

                    self.state = 'main_game'

                if level_button.action():
                    print("levels selector")
                    self.state = 'levels'

        menu_screen.draw(screen)
        play_button.draw(screen)
        quit_button.draw(screen)
        level_button.draw(screen)
        pygame.display.flip()
        self.map.image = pygame.transform.scale(self.map.image, (screen_w - 200, screen_h))
        self.map.draw(screen)
        self.bar.draw(screen)
        crosshairGroup.update()

    def select_level(self):
        pygame.mouse.set_visible(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = 'intro'

    def main_game(self):

        pygame.mouse.set_visible(False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shot()
                kill_target()
                self.place_selected_weapon()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = 'intro'

        for elem in targetGroup:
            elem.move()
            if elem.rect.y > 810:
                self.state = 'intro'

        if len(targetGroup) == 0:
            self.state = 'intro'

        pygame.display.flip()
        self.map.draw(screen)
        targetGroup.draw(screen)
        self.bar.draw(screen)
        self.weapon_menager.draw(screen)
        crosshairGroup.draw(screen)
        crosshairGroup.update()

        self.bar.action()

#main-game methods !!! Pozniej damy to do odosobnionej klasy!!!

    def set_selected_weapon(self, weapon_type):
        self.selected_weapon = weapon_type;
        crosshair.tower_picture(ImagesPaths().weapons[weapon_type])


    def place_selected_weapon(self):
        pos_x, pos_y = pygame.mouse.get_pos()
        if pos_x < screen_w - 200:
            if self.selected_weapon != -1:
                self.weapon_menager.add_weapon(self.selected_weapon, pos_x, pos_y)
                self.selected_weapon = -1
                crosshair.standard_crosshair("./assets/aim.png")

#koniec main-game




pygame.init()
clock = pygame.time.Clock()

# game
game_stage = GameState()

# game screen
screen_w = 1400
screen_h = 800
screen = pygame.display.set_mode((screen_w, screen_h))

# intro screen
menu_screen = Menu(screen_w / 2 - 100, screen_h / 2 - 200, 200, 400)

# crosshair
crosshair = Crosshair("./assets/aim.png")
crosshairGroup = pygame.sprite.Group()
crosshairGroup.add(crosshair)

# targets
targetGroup = pygame.sprite.Group()

# kill
def kill_target():
    pygame.sprite.spritecollide(crosshair, targetGroup, True)


while True:
    game_stage.state_manager()
    clock.tick(60)
