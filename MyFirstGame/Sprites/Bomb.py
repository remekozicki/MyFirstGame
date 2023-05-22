import pygame

from MyFirstGame.ImagesPaths import ImagesPaths


class Bomb(pygame.sprite.Sprite):

    def __init__(self, bomb_type, pos_x, pos_y ):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.set_bomb_attributes(bomb_type)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def set_bomb_attributes(self, bomb_type):
        image_paths = ImagesPaths()

        if bomb_type == 3:
            self.image = pygame.image.load(image_paths.weapons[3])
            image_w = self.image.get_width()
            image_h = self.image.get_height()
            self.image = pygame.transform.scale(self.image, (int(image_w*0.1), int(image_h*0.1)))
            self.damage = 5
            self.range = 100
            self.price = 50


        elif bomb_type == 4:
            self.image = pygame.image.load(image_paths.weapons[4])
            image_w = self.image.get_width()
            image_h = self.image.get_height()
            self.image = pygame.transform.scale(self.image, (int(image_w * 0.1), int(image_h * 0.1)))
            self.damage = 15
            self.range = 200
            self.price = 100

        # elif bomb_type == 5:
        #     self.image = pygame.image.load(image_paths.weapons[5])
        #     image_w = self.image.get_width()
        #     image_h = self.image.get_height()
        #     self.image = pygame.transform.scale(self.image, (int(image_w * 0.1), int(image_h * 0.1)))
        #     self.damage = 20
        #     self.range = 250
        #     self.price = 200

        else:
            print("error in bomb class - wrong type")


