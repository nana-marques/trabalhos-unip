from pygame import *
import pygame
import sys

pygame.init()

width = 800
height = 720
white = (255, 255, 255)
black = (0, 0, 0)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dancing Benq")

image = "p2.png"
try:
    image = pygame.image.load(image)
except pygame.error:
    print("Erro de carregamento")
    pygame.quit()
    sys.exit()

image_rect = image.get_rect()
image_flip = image
image_move = image_rect

while True:
    window.fill(white)
    jump = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                image_flip = pygame.transform.flip(image, False, False)
                # image_move.move_ip(10, 700)
            
            elif event.key == pygame.K_LEFT:
                image_flip = pygame.transform.flip(image, True, False)
                # image_move.move_ip(300, 700)

            elif event.key == pygame.K_UP:
                image_flip = pygame.transform.flip(image, True, False)
                jump = True
                # image_move.move_ip(300, 700)

    window.blit(image_flip, (200, 10) if jump else (200, 100))

    pygame.display.flip()