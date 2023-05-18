import pygame

class Endgame:
    def __init__(self):
        self.image = pygame.image.load("../assets/game_over.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def draw(self, screen):
        screen.blit(self.image, self.rect)
