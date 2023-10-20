import pygame


class Fish(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/orange_fish.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.x = x
        self.y = y
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        print("I am a brand new fish")

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


    def update(self):
        if self.moving_left:
            self.x -= 2
        elif self.moving_right:
            self.x += 2
        if self.moving_up:
            self.y -= 2
        elif self.moving_down:
            self.y += 2
