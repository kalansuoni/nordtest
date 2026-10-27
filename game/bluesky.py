import pygame
import sys


pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Blue Sky")


blue = (135, 206, 235)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

   
    screen.fill(blue)

    
    pygame.display.flip()