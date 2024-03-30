import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SPEED = 5
SCORE = 0

font_small = pygame.font.SysFont("Verdana", 20)
game_over = font_small.render("Game Over", True, BLACK)

DISPLAYSURF = pygame.display.set_mode((1400, 1000))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab8/blue.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 950)
        self.speed = 0

    def update(self):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def move_left(self):
        self.speed = -5

    def move_right(self):
        self.speed = 5

    def stop(self):
        self.speed = 0

class Car(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.image.load(f"lab8/{color}.png")
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.reset()

player = Player()
all_sprites = pygame.sprite.Group()
cars = pygame.sprite.Group()

all_sprites.add(player)

for color in ['red', 'red_2', 'yellow', 'yellow_2']:
    car = Car(color)
    all_sprites.add(car)
    cars.add(car)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move_left()
            elif event.key == K_RIGHT:
                player.move_right()
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.stop()

    all_sprites.update()

    if pygame.sprite.spritecollide(player, cars, False):
        running = False

    DISPLAYSURF.fill(WHITE)
    all_sprites.draw(DISPLAYSURF)

    pygame.display.flip()
    FramePerSec.tick(FPS)

pygame.quit()
sys.exit()
