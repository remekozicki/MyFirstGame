import pygame


class Bombs(pygame.sprite.Sprite):

    def __init__(self, pic_path, damage, range_radius):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.damage = damage
        self.range = range_radius
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)


