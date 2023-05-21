import pygame


class Crosshair(pygame.sprite.Sprite):

    def __init__(self, pic_path):
        super().__init__()
        self.standard_crosshair(pic_path)
        self.rect = self.image.get_rect()

    def standard_crosshair(self, pic_path):
        self.image = pygame.image.load(pic_path)
        self.image = pygame.transform.scale(self.image, (40, 40))

    def tower_picture(self, pic_path):
        self.image = pygame.image.load(pic_path)
        image_w = self.image.get_width()
        image_h = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(image_w * 0.1), int(image_h * 0.1)))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

