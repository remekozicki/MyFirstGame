import pygame
import random
import sys
from Crosshair import Crosshair
from Target import Target
from Button import Button

class GameState():

    def __init__(self):
        self.state = 'intro'

    def intro(self):

        pygame.mouse.set_visible(True)

        play_button.draw(screen)
        quit_button.draw(screen)

        if quit_button.action():
            print('quit')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.action():
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.action():
                    self.state = 'main_game'
                    play_button.clicked = False

        pygame.display.flip()
        screen.blit(background, (0, 0))
        screen.blit(readyText, (screen_w / 2 - 100, screen_h / 2 - 100))
        crosshairGroup.update()

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()

    def main_game(self):

        pygame.mouse.set_visible(False)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shot()
                kill_target()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = 'intro'

        pygame.display.flip()
        screen.blit(background, (0, 0))
        targetGroup.draw(screen)
        crosshairGroup.draw(screen)
        crosshairGroup.update()


pygame.init()
clock = pygame.time.Clock()

# game
game_stage = GameState()

# game screen
screen_w = 1200
screen_h = 800
screen = pygame.display.set_mode((screen_w, screen_h))


# intro screen
readyText = pygame.image.load("./assets/startgame.png")
readyText = pygame.transform.scale(readyText, (200, 200))

# crosshair
crosshair = Crosshair("./assets/aim.png")
crosshairGroup = pygame.sprite.Group()
crosshairGroup.add(crosshair)

# bg
background = pygame.image.load("./assets/bg001.png")
background = pygame.transform.scale(background, (screen_w, screen_h))

# targets
targetGroup = pygame.sprite.Group()

#buttons
play_button = Button(100, 200, 0.5, "./assets/orange button/Play orange button 300x80.png")
quit_button = Button(100, 400, 0.5, "./assets/orange button/Quit orange button 300x80.png")

for _ in range(20):
    newT = Target("./assets/new_bullet.png", random.randrange(0, screen_w), random.randrange(0, screen_h))
    targetGroup.add(newT)


# kill
def kill_target():
    pygame.sprite.spritecollide(crosshair, targetGroup, True)


while True:
    game_stage.state_manager()
    clock.tick(60)
