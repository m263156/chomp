import pygame
import sys
import random
import fish
import minnow
from settings import *

pygame.init()
# Builds Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
# Assets
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
sand_top.set_colorkey((0, 0, 0))
seagrass = pygame.image.load("assets/images/seagrass.png").convert()
seagrass.set_colorkey((0, 0, 0))
game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", TEXT_SIZE)

my_fish = fish.Fish(200, 200)
my_minnows = []
for _ in range(NUM_MINNOWS):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT - 2 * TILE_SIZE)
    my_minnows.append(minnow.Minnow(x, y))

background = screen.copy()

clock = pygame.time.Clock()


def draw_background():
    background.fill(WATER_COLOR)
    # Builds Bottom Sand
    for i in range(SCREEN_WIDTH//TILE_SIZE):
        background.blit(sand, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))
    # Builds Top Sand
    for i in range(SCREEN_WIDTH//TILE_SIZE):
        background.blit(sand_top, (i * TILE_SIZE, SCREEN_HEIGHT - (2*TILE_SIZE)))
    # Places 4 Seaweeds Randomly
    for i in range(4):
        x = random.randint(0, SCREEN_WIDTH - (2*TILE_SIZE))
        y = random.randint(SCREEN_HEIGHT - 2.5 * TILE_SIZE, SCREEN_HEIGHT - 0.5 * TILE_SIZE)
        background.blit(seagrass, (x, y))
    # Add Text
    title = game_font.render("Chomp!", True, (255, 0, 0))
    background.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, SCREEN_HEIGHT//2 - title.get_height()//2))
    pygame.display.flip()


draw_background()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("thanks for playing!")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = True
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = True
            if event.key == pygame.K_UP:
                my_fish.moving_up = True
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                my_fish.moving_left = False
            if event.key == pygame.K_RIGHT:
                my_fish.moving_right = False
            if event.key == pygame.K_UP:
                my_fish.moving_up = False
            if event.key == pygame.K_DOWN:
                my_fish.moving_down = False
    screen.blit(background, (0, 0))
    my_fish.update()
    my_fish.draw(screen)
    for my_minnow in my_minnows:
        my_minnow.draw(screen)
    pygame.display.flip()
    clock.tick(60)
