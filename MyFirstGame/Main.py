import pygame

from Screens.MyFirstGame import GameState

if __name__ == '__main__':

    pygame.init()
    clock = pygame.time.Clock()

    # game
    game_stage = GameState()

    while 1:
        game_stage.state_manager()
        clock.tick(60)
