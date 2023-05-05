import pygame
import random
import sys
from Crosshair import Crosshair
from Map import Map
from Bar import Bar
from WeaponMenager import WeaponMenager

crosshairGroup = pygame.sprite.Group()


class MainGame:
    def __init__(self):
        self.targetGroup = pygame.sprite.Group()
        self.map = Map(0)
        self.bar = Bar()
        self.weapon_menager = WeaponMenager()
        self.crosshair = Crosshair("./assets/aim.png")


    def draw(self, screen):
        self.map.draw(screen)
        self.targetGroup.draw(screen)
        self.bar.draw(screen)
        self.weapon_menager.draw(screen)
        crosshairGroup.draw(screen)

    def kill_target(self):
        pygame.sprite.spritecollide(self.crosshair, self.targetGroup, True)

    def update(self):

        pygame.mouse.set_visible(False)

        # crosshair

        crosshairGroup.add(self.crosshair)

        # targets
        targetGroup = pygame.sprite.Group()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.crosshair.shot()
                self.kill_target()
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
        crosshairGroup.update()

