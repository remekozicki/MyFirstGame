import pygame
import random
import sys
import math

from MyFirstGame.Menagers.WeaponMenager import WeaponMenager
from MyFirstGame.Screens.Bar import Bar
from MyFirstGame.Sprites.Crosshair import Crosshair
from MyFirstGame.Sprites.Map import Map
from MyFirstGame.Sprites.Target import Target
from MyFirstGame.Sprites.Tower import Tower
from MyFirstGame.ImagesPaths import ImagesPaths


class MainGame:
    def __init__(self, screen, game):

        self.game = game
        self.map = Map(0)
        self.weapon_menager = WeaponMenager()

        self.screen_w = 1400
        self.screen_h = 800
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))

        self.bar = Bar(self)
        self.selected_weapon = -1

        self.crosshair = Crosshair("assets/aim.png")
        self.crosshairGroup = pygame.sprite.Group()
        self.crosshairGroup.add(self.crosshair)

        self.targets_to_kill = []
        self.money = 100

        # self.drawGrid()

    def drawGrid(self):
        blockSize = 40
        for x in range(0, self.screen_w - 200, blockSize):
            for y in range(0, self.screen_h, blockSize):
                gridRect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.screen, (200, 200, 200), gridRect, 1)

    def start_game(self):
        self.targetGroup = pygame.sprite.Group()
        self.weapon_menager.clear_weapopns()
        self.money = 100

        for i in range(20):
            newT = Target(-random.randrange(0, 100) * 5, 0, self.map.path, 0)
            self.targetGroup.add(newT)

    def render(self):
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.crosshair.shot()
                self.kill_target()
                self.place_selected_weapon()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.set_state('intro')

        for elem in self.targetGroup:
            elem.move()
            if elem.rect.y > 810:
                self.game.set_state('intro')

        if len(self.targetGroup) == 0:
            self.game.set_state('intro')

        pygame.display.flip()
        self.map.image = pygame.transform.scale(self.map.image, (self.screen_w - 200, self.screen_h))
        self.map.draw(self.screen)
        self.targetGroup.draw(self.screen)
        self.bar.draw(self.screen)
        self.weapon_menager.draw(self.screen)
        self.crosshairGroup.draw(self.screen)
        self.crosshairGroup.update()
        self.bar.action()
        self.find_targets_in_range()
        self.drawGrid()

    def set_selected_weapon(self, weapon_type):
        self.selected_weapon = weapon_type
        self.crosshair.tower_picture(ImagesPaths().weapons[weapon_type])

    def place_selected_weapon(self):
        pos_x, pos_y = pygame.mouse.get_pos()
        grid_x = pos_x // 40
        grid_y = pos_y // 40


        if pos_x < self.screen_w - 200:
            if self.map.gridArray[grid_y][grid_x] == 0:
                print(grid_x, grid_y)
                if self.selected_weapon != -1:
                    tower_price = Tower(self.selected_weapon, pos_x, pos_y).price
                    if self.money - tower_price >= 0:
                        self.weapon_menager.add_weapon(self.selected_weapon, pos_x, pos_y)
                        self.money -= tower_price
                        self.selected_weapon = -1
                        self.crosshair.standard_crosshair("assets/aim.png")


    def kill_target(self):
        pygame.sprite.spritecollide(self.crosshair, self.targetGroup, True)

    def set_selected_map(self, map_type):
        self.map = Map(map_type)
        print("mg", map_type)

    def find_targets_in_range(self):
        for tower in self.weapon_menager.towers:
            for target in self.targetGroup:
                if math.sqrt((target.rect.x - tower.pos_x)**2 + (target.rect.y - tower.pos_y)**2) < tower.range:
                    if tower.is_ready_to_shot():
                        target.kill()
                        self.money += target.money_per_kill
                        print("in range")

    def kill_targets_in_range(self):
        for target in self.targets_to_kill:
            self.targetGroup.remove(target)




