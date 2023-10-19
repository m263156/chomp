import pygame
import sys
import random
from settings import *

pygame.init()

game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", TEXT_SIZE)
# Builds Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)
# Sand Rectangle
pygame.draw.rect(screen,
                 SAND_COLOR,
                 (0, SCREEN_HEIGHT-SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))
# Assets
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
sand_top.set_colorkey((0, 0, 0))
seagrass = pygame.image.load("assets/images/seagrass.png").convert()
seagrass.set_colorkey((0, 0, 0))
# Builds Bottom Sand
for i in range(SCREEN_WIDTH//TILE_SIZE):
    screen.blit(sand, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))
# Builds Top Sand
for i in range(SCREEN_WIDTH//TILE_SIZE):
    screen.blit(sand_top, (i * TILE_SIZE, SCREEN_HEIGHT - (2*TILE_SIZE)))
# Places 4 Seaweeds Randomly
for i in range(4):
    x = random.randint(0, SCREEN_WIDTH - (2*TILE_SIZE))
    y = random.randint(SCREEN_HEIGHT - 2.5 * TILE_SIZE, SCREEN_HEIGHT - 0.5 * TILE_SIZE)
    screen.blit(seagrass, (x, y))
# Add Text
title = game_font.render("Chomp!", True, (255, 0, 0))
screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, SCREEN_HEIGHT//2 - title.get_height()//2))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("thanks for playing!")
            pygame.quit()
            sys.exit()
