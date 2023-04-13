import pygame
import sys

# general setup
pygame.init()
clock = pygame.time.Clock()

# display surface
screen = pygame.display.set_mode((1200, 800))
screen2 = pygame.Surface([100, 200])
screen2.fill((0, 0, 255))

target = pygame.image.load("./MyFirstGame/assets/new_bullet.png")
target = pygame.transform.scale(target, (100, 100))
target_rect = target.get_rect(topleft = [100, 200])
print(target_rect.center)



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    screen.blit(screen2, (0, 50))
    screen.blit(target, target_rect)
    target_rect.right += 1

    pygame.display.flip()  # draws everything form the loop
    clock.tick(60 )
