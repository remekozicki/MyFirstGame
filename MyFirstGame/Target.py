import pygame


class Target(pygame.sprite.Sprite):

    def __init__(self, pic_path, pos_x, pos_y):
        super().__init__()
        # self.pos_x = pos_x
        # self.pos_y = pos_y
        self.image = pygame.image.load(pic_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def draw(self, screen):
        screen.blit(self.image, self.rect)



