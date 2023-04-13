import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

curr_time = 0
button_p_time = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            button_p_time = pygame.time.get_ticks()
            screen.fill((255, 255, 255))

    curr_time = pygame.time.get_ticks()

    if curr_time - button_p_time > 2000:
        screen.fill((0, 0, 0))

    print(f"current time {curr_time} button time {button_p_time}")

    pygame.display.flip()
    clock.tick(60)


