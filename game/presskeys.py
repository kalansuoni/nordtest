import sys
import pygame


pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Key Test")


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            print(event.key)

    screen.fill((255, 255, 255))
    pygame.display.flip()