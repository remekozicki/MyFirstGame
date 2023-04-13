import pygame


class Crosshair(pygame.sprite.Sprite):

    def __init__(self, pic_path):
        super().__init__()
        self.image = pygame.image.load(pic_path)
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.shotSound = pygame.mixer.Sound("./assets/gunshot_1.wav")

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shot(self):
        self.shotSound.play()

