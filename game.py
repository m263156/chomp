import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Chomp!")
screen.fill((100,100,150))
pygame.draw.rect(screen, (100,25,0), (0, 380, 400, 400))
pygame.draw.rect(screen, (0,150,0), (250, 50, 50, 50))
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (200,200, 64, 64))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("thanks for playing!")
            pygame.quit()
            sys.exit()