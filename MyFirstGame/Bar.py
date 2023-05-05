import pygame


class Bar:
    def __init__(self):

        self.image = pygame.image.load("./assets/woodBar.jpg")
        self.image = pygame.transform.rotate(self.image, 90)
        self.image = pygame.transform.scale(self.image, (200, 800))

        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

