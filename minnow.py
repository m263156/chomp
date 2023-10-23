import pygame


class Minnow(pygame.sprite.Sprite):

    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/minnow.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.x = x
        self.y = y
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = True
        self.moving_right = False
        self.moving_up = False
        self.moving_down = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left:
            self.rect.x -= 2
        elif self.moving_right:
            self.rect.x += 2
        if self.moving_up:
            self.rect.y -= 2
        elif self.moving_down:
            self.rect.y += 2
        if self.rect.left < 0:
            self.rect.left = 0
            self.moving_right = True
            self.moving_left = False
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT - 2 * TILE_SIZE:
            self.rect.bottom = SCREEN_HEIGHT - 2 * TILE_SIZE
