import pygame
# import random
import sys

# from MyFirstGame.ImagesPaths import ImagesPaths
# # from MyFirstGame.MyFirstGame.Menagers.WeaponMenager import WeaponMenager
# from MyFirstGame.Screens.MainGame import MainGame
# from MyFirstGame.Screens.Menu import Menu
# from MyFirstGame.Sprites.Button import Button
# # from MyFirstGame.MyFirstGame.Sprites.Crosshair import Crosshair
# from MyFirstGame.Screens.Bar import Bar
# from MyFirstGame.Screens.LevelsMenu import LevelsMenu
# from MyFirstGame.Sprites.Map import Map
# # from MyFirstGame.MyFirstGame.Sprites.Target import Target

from ImagesPaths import ImagesPaths
from Screens.LevelsMenu import LevelsMenu
from Screens.MainGame import MainGame
from Sprites.Map import Map
from Sprites.Button import Button
from Screens.Menu import Menu

class GameState():

    def __init__(self):
        self.image_paths = ImagesPaths()
        self.state = 'intro'

        self.selected_map = 0
        self.map = Map(self.selected_map)

        # game screen
        self.screen_w = 1400
        self.screen_h = 800
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))



        # intro screen
        self.menu_screen = Menu(self.screen_w / 2 - 100, self.screen_h / 2 - 200, 200, 400)

        self.main_game_test = MainGame(self.screen, self)
        # levels screen
        self.levels_screen = LevelsMenu(self.screen_w / 2 - 150, self.screen_h / 2 - 300, 300, 600, self.main_game_test, self)

        self.bar = self.main_game_test.bar

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game_test.render()
            #self.main_game()
        if self.state == 'levels':
            self.select_level()


    def set_state(self, state):
        self.state = state

    def intro(self):
        pygame.mouse.set_visible(True)
        # logo XD
        # logo = pygame.image.load("./assets/logo.png")
        # logo = pygame.transform.scale(logo, (250, 250))
        # buttons
        play_button = Button(self.screen_w / 2 - 75, self.screen_h / 2 - 150, 0.5,
                             "./assets/orange button/Play orange button 300x80.png")
        quit_button = Button(self.screen_w / 2 - 75, self.screen_h / 2 + 100, 0.5,
                             "./assets/orange button/Quit orange button 300x80.png")
        level_button = Button(self.screen_w / 2 - 75, self.screen_h / 2, 0.5,
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
                    # self.targetGroup = pygame.sprite.Group()
                    self.main_game_test.start_game()

                    #usun
                    # for i in range(20):
                    #     newT = Target("assets/new_bullet.png", -random.randrange(0, 100) * 5, 0, self.map.path)
                    #     self.targetGroup.add(newT)
                    #usun-end

                    self.state = 'main_game'

                if level_button.action():
                    print("levels selector")
                    self.state = 'levels'

        self.menu_screen.draw(self.screen)
        play_button.draw(self.screen)
        quit_button.draw(self.screen)
        level_button.draw(self.screen)
        pygame.display.flip()
        self.map.image = pygame.transform.scale(self.map.image, (self.screen_w - 200, self.screen_h))
        self.map.draw(self.screen)
        self.bar.draw(self.screen)

        # self.crosshairGroup.add(self.crosshair)

    def select_level(self):
        pygame.mouse.set_visible(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = 'intro'

        pygame.display.flip()
        self.map.image = pygame.transform.scale(self.map.image, (self.screen_w - 200, self.screen_h))
        self.map.draw(self.screen)
        self.levels_screen.draw(self.screen)
        self.levels_screen.action(self.main_game_test)
        self.levels_screen.action(self)

    def set_selected_map(self, map_type):
        self.map = Map(map_type)
        print("sm", map_type)



