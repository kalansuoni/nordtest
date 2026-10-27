import sys
import pygame


class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

       
        self.image = pygame.image.load("rocket.bmp")
        self.rect = self.image.get_rect()

        
        self.rect.center = self.screen_rect.center

        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.speed = 0.25

        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Update rocket position."""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rocket")

bg_color = (135, 206, 235)

rocket = Rocket(screen)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = True
            elif event.key == pygame.K_UP:
                rocket.moving_up = True
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = False
            elif event.key == pygame.K_UP:
                rocket.moving_up = False
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = False

    rocket.update()

    screen.fill(bg_color)
    rocket.blitme()

    pygame.display.flip()