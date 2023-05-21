import pygame

class Endgame:
    def __init__(self):
        self.font = pygame.font.Font('assets/Silkscreen/slkscre.ttf', 100)
        self.text = self.font.render('', False, (255, 255, 255))
        self.textBG = self.font.render('', False, (0, 0, 0))


    def draw(self, screen):
        screen.blit(self.textBG, (305, 205))
        screen.blit(self.text, (300, 200))


    def set_result(self, res):
        if res:
            self.text = self.font.render('YOU WIN!', False, (255, 255, 255))
            self.textBG = self.font.render('YOU WIN!', False, (0, 0, 0))
        else:
            self.text = self.font.render('YOU LOSE :(', False, (255, 255, 255))
            self.textBG = self.font.render('YOU LOSE :(', False, (0, 0, 0))










