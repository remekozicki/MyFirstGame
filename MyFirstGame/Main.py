import pygame

from MyFirstGame.Screens.MyFirstGame import GameState


if __name__ == '__main__':

    pygame.init()
    clock = pygame.time.Clock()

    # game
    game_stage = GameState()

    while True:
        game_stage.state_manager()
        clock.tick(60)
