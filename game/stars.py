from random import randint

import sys
import pygame

from star import Star

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Stars")


star = Star(screen)

stars = []


star_width = star.rect.width
star_height = star.rect.height

current_x = star_width
current_y = star_height

while current_y < (800 - 2 * star_height):
    while current_x < (1200 - 2 * star_width):
        new_star = Star(screen)
    
        
        random_x = randint(-40, 40)
        random_y = randint(-40, 40)

        new_star.rect.x = current_x + random_x
        new_star.rect.y = current_y + random_y

        stars.append(new_star)

        current_x += 2 * star_width

    current_x = star_width
    current_y += 2 * star_height



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    for star in stars:
        star.draw_star()

    pygame.display.flip()