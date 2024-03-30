import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)

RADIUS = 25
x = SCREEN_WIDTH // 2
y = SCREEN_HEIGHT // 2

SPEED = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moving Ball")

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (x, y), RADIUS)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if y - SPEED >= RADIUS:
                    y -= SPEED
            elif event.key == pygame.K_DOWN:
                if y + SPEED <= SCREEN_HEIGHT - RADIUS:
                    y += SPEED
            elif event.key == pygame.K_LEFT:
                if x - SPEED >= RADIUS:
                    x -= SPEED
            elif event.key == pygame.K_RIGHT:
                if x + SPEED <= SCREEN_WIDTH - RADIUS:
                    x += SPEED

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
