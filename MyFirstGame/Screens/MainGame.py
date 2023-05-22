import pygame
import random
import sys
import math

from MyFirstGame.Menagers.WavesMenager import WavesMenager
from MyFirstGame.Menagers.WeaponMenager import WeaponMenager
from MyFirstGame.Screens.Bar import Bar
from MyFirstGame.Sprites.Bomb import Bomb
from MyFirstGame.Sprites.Crosshair import Crosshair
from MyFirstGame.Sprites.Map import Map
from MyFirstGame.Sprites.Target import Target
from MyFirstGame.Sprites.Tower import Tower
from MyFirstGame.ImagesPaths import ImagesPaths


START_MONEY = 1000

class MainGame:
    def __init__(self, screen, game):

        self.game = game
        self.map = Map(0)
        self.weapon_menager = WeaponMenager()
        self.wave_menager = WavesMenager()
        self.shotSound = pygame.mixer.Sound("assets/gunshot_1.wav")


        self.screen_w = 1400
        self.screen_h = 800
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))

        self.bar = Bar(self)
        self.selected_weapon = -1

        self.crosshair = Crosshair("assets/shovel.png")
        self.crosshairGroup = pygame.sprite.Group()
        self.crosshairGroup.add(self.crosshair)

        self.targets_to_kill = []
        self.money = START_MONEY
        self.lives = 3
        # self.drawGrid()'
        self.winning = True




    def drawGrid(self):
        blockSize = 40
        for x in range(0, self.screen_w - 200, blockSize):
            for y in range(0, self.screen_h, blockSize):
                gridRect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.screen, (200, 200, 200), gridRect, 1)


    def start_game(self):
        self.targetGroup = pygame.sprite.Group()
        self.weapon_menager.clear_weapopns()
        self.reset_values()

    def reset_values(self):
        self.money = START_MONEY
        self.selected_weapon = -1
        self.lives = 3
        self.wave_menager.wave_index = 0


    def render(self):
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.remove_selected_weapon()
                self.place_selected_weapon()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.set_state('intro')

        for elem in self.targetGroup:
            elem.move()
            if elem.rect.y > 800 or elem.rect.x > 1200:
                self.lives -= 1
                self.targetGroup.remove(elem)
                if self.lives == 0:
                    self.winning = False
                    self.game.set_state('end_game')
                    print("YOU LOST GAME")


        if len(self.targetGroup) == 0:
            if self.wave_menager.is_there_more_waves():
                wave = self.wave_menager.get_new_wave()
                for type in wave:
                    newT = Target(-random.randrange(0, len(wave)*10) * 5, 0, self.map.path, type)
                    self.targetGroup.add(newT)
            else:
                self.winning = True
                self.game.set_state('end_game')
                print("YOU WON GAME!!!!")

        pygame.display.flip()
        self.map.image = pygame.transform.scale(self.map.image, (self.screen_w - 200, self.screen_h))
        self.map.draw(self.screen)
        # self.targetGroup.draw(self.screen)

        for target in self.targetGroup:
            target.draw(self.screen)

        self.bar.draw(self.screen)
        self.weapon_menager.draw_towers(self.screen)
        self.weapon_menager.bombs.draw(self.screen)

        self.crosshairGroup.draw(self.screen)

        self.crosshairGroup.update()
        self.bar.action()
        self.find_targets_in_range()
        self.find_targets_on_bomb()

        # self.drawGrid()
    def set_selected_weapon(self, weapon_type):
        self.selected_weapon = weapon_type
        self.crosshair.tower_picture(ImagesPaths().weapons[weapon_type])

    def place_selected_weapon(self):
        pos_x, pos_y = pygame.mouse.get_pos()
        grid_x = pos_x // 40
        grid_y = pos_y // 40

        if pos_x < self.screen_w - 200:
            if self.selected_weapon != -1:
                if self.selected_weapon <= 2:
                    if self.map.gridArray[grid_y][grid_x] == 0:
                        weapon_price = Tower(self.selected_weapon, pos_x, pos_y).price
                        if self.money - weapon_price >= 0:
                            self.weapon_menager.add_weapon(self.selected_weapon, pos_x, pos_y)
                            self.money -= weapon_price
                            self.selected_weapon = -1
                            self.crosshair.standard_crosshair("assets/shovel.png")
                else:
                    if self.map.gridArray[grid_y][grid_x] == 1:
                        weapon_price = Bomb(self.selected_weapon, pos_x, pos_y).price
                        if self.money - weapon_price >= 0:
                            self.weapon_menager.add_weapon(self.selected_weapon, pos_x, pos_y)
                            self.money -= weapon_price
                            self.selected_weapon = -1
                            self.crosshair.standard_crosshair("assets/shovel.png")

    def remove_selected_weapon(self):
        pos_x, pos_y = pygame.mouse.get_pos()

        if pos_x > self.screen_w - 200:
            self.selected_weapon = -1
            self.crosshair.standard_crosshair("assets/shovel.png")


    def set_selected_map(self, map_type):
        self.map = Map(map_type)

    def find_targets_in_range(self):
        for tower in self.weapon_menager.towers:
            for target in self.targetGroup:
                if math.sqrt((target.rect.x - tower.pos_x)**2 + (target.rect.y - tower.pos_y)**2) < tower.range:
                    if tower.is_ready_to_shot():
                        target.hp -= tower.damage
                        self.shotSound.play()
                        if(target.hp <= 0):
                                target.kill()
                                self.money += target.money_per_kill


    def find_targets_on_bomb(self):
        for index, bomb in enumerate(self.weapon_menager.bombs):
            for target in self.targetGroup:
                if math.sqrt((target.rect.x - bomb.pos_x)**2 + (target.rect.y - bomb.pos_y)**2) < bomb.range:
                    target.kill()
                    self.money += target.money_per_kill
                    bomb.kill()


    def kill_targets_in_range(self):
        for target in self.targets_to_kill:
            self.targetGroup.remove(target)




