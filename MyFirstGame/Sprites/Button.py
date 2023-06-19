import pygame

class Button():

    def __init__(self, pos_x, pos_y, scale, pic_path):
        self.scale = scale
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.image.load(pic_path).convert_alpha()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.width * self.scale), int(self.height*self.scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)
        self.clicked = False

    def draw(self, surface):
        surface.blit(self.image, (self.pos_x, self.pos_y))

    def action(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
