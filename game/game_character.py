import pygame
import sys


class Character:
    def __init__(self, screen):
        self.screen = screen

        
        self.image = pygame.image.load("character.bmp")

        
        self.image.set_colorkey((255, 255, 255))

        
        self.rect = self.image.get_rect()

        
        self.rect.center = screen.get_rect().center

    def draw_character(self):
        self.screen.blit(self.image, self.rect)



pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Character")


bg_color = (255, 255, 255)


character = Character(screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(bg_color)

    character.draw_character()

    pygame.display.flip()