import pygame
import time

print(f"the quit event is {pygame.QUIT}")
pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Chomp!")
screen.fill((100,100,150))
pygame.draw.rect(screen, (100,25,0), (0, 380, 400, 400))
pygame.draw.rect(screen, (0,150,0), (250, 50, 50, 50))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("nice try")