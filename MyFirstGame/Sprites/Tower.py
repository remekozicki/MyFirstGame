import pygame

from MyFirstGame.MyFirstGame.ImagesPaths import ImagesPaths


class Tower(pygame.sprite.Sprite):

    def __init__(self, tower_type, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.set_tower_attributes(tower_type)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def set_tower_attributes(self, tower_type):
        image_paths = ImagesPaths()

        if tower_type == 0:
            self.image = pygame.image.load(image_paths.weapons[0])
            image_w = self.image.get_width()
            image_h = self.image.get_height()
            self.image = pygame.transform.scale(self.image, (int(image_w*0.1), int(image_h*0.1)))
            self.damage = 5
            self.range = 100
        elif tower_type == 1:
            self.image = pygame.image.load(image_paths.weapons[1])
            image_w = self.image.get_width()
            image_h = self.image.get_height()
            self.image = pygame.transform.scale(self.image, (int(image_w * 0.1), int(image_h * 0.1)))
            self.damage = 15
            self.range = 200
        elif tower_type == 2:
            self.image = pygame.image.load(image_paths.weapons[2])
            image_w = self.image.get_width()
            image_h = self.image.get_height()
            self.image = pygame.transform.scale(self.image, (int(image_w * 0.1), int(image_h * 0.1)))
            self.damage = 20
            self.range = 250
        else:
            print("error in tower class - wrong type")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

