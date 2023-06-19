import pygame


class Menu():

    def __init__(self, pos_x, pos_y, width, height):
        self.image = pygame.image.load("assets/woodBar.jpg").convert()
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
