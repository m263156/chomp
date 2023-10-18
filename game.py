import pygame
import sys

TILE_SIZE = 64
SCREEN_WIDTH = 16 * TILE_SIZE
SCREEN_HEIGHT = 9 * TILE_SIZE
SAND_HEIGHT = 20
WATER_COLOR = (114, 159, 232)
SAND_COLOR = (135, 128, 107)
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)

pygame.draw.rect(screen,
                 SAND_COLOR,
                 (0, SCREEN_HEIGHT-SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
for i in range(SCREEN_WIDTH//TILE_SIZE):
    screen.blit(sand, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))
for i in range(SCREEN_WIDTH//TILE_SIZE):
    screen.blit(sand_top, (i * TILE_SIZE, SCREEN_HEIGHT - (2*TILE_SIZE)))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("thanks for playing!")
            pygame.quit()
            sys.exit()
