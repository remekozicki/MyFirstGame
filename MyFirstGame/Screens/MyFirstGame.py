import pygame
# import random
import sys

from MyFirstGame.ImagesPaths import ImagesPaths
from MyFirstGame.Screens.LevelsMenu import LevelsMenu
from MyFirstGame.Screens.MainGame import MainGame
from MyFirstGame.Sprites.Map import Map
from MyFirstGame.Sprites.Button import Button
from MyFirstGame.Screens.Menu import Menu
from MyFirstGame.Screens.EndGame import Endgame
from pygame.locals import *


class GameState():

    def __init__(self):
        self.image_paths = ImagesPaths()
        self.state = 'intro'

        self.selected_map = 0

        # game screen
        self.screen_w = 1400
        self.screen_h = 800
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

        self.map = Map(self.selected_map)

        # intro screen
        self.menu_screen = Menu(self.screen_w / 2 - 100, self.screen_h / 2 - 200, 200, 400)

        self.main_game = MainGame(self.screen, self)
        # levels screen
        self.levels_screen = LevelsMenu(self.screen_w / 2 - 150, self.screen_h / 2 - 300, 300, 600,
                                        self.main_game, self)
        # bar
        self.bar = self.main_game.bar
        # endgame
        self.endGame = Endgame()

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game.render()
            # self.main_game()
        if self.state == 'levels':
            self.select_level()
        if self.state == 'end_game':
            self.end_game()

    def set_state(self, state):
        self.state = state

    def intro(self):
        pygame.mouse.set_visible(True)

        play_button = Button(self.screen_w / 2 - 75, self.screen_h / 2 - 130, 0.5,
                             "./assets/orange button/Play orange button 300x80.png")
        quit_button = Button(self.screen_w / 2 - 75, self.screen_h / 2 + 70, 0.5,
                             "./assets/orange button/Quit orange button 300x80.png")
        level_button = Button(self.screen_w / 2 - 75, self.screen_h / 2 - 30, 0.5,
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

                    self.main_game.start_game()

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

    def end_game(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = 'intro'
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'intro'

        self.endGame.set_result(self.main_game.winning)
        self.endGame.draw(self.screen)
        pygame.display.flip()

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
        self.levels_screen.action(self.main_game)
        self.levels_screen.action(self)

    def set_selected_map(self, map_type):
        self.map = Map(map_type)
