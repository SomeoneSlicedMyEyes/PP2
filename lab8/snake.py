import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
SNAKE_SPEED = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.level = 1
        self.food = self.generate_food()

    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction
        new_head = ((x + dx * CELL_SIZE) % WIDTH, (y + dy * CELL_SIZE) % HEIGHT)
        if new_head in self.body[1:] or self.check_border_collision(new_head):
            return False
        self.body.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            if self.score % 3 == 0:
                self.level += 1
            self.food = self.generate_food()
        else:
            self.body.pop()
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def generate_food(self):
        while True:
            food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                    random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
            if food not in self.body:
                return food

    def check_border_collision(self, position):
        return position[0] < 0 or position[0] >= WIDTH or position[1] < 0 or position[1] >= HEIGHT

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(surface, RED, (self.food[0], self.food[1], CELL_SIZE, CELL_SIZE))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()

    snake = Snake()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        if not snake.move():
            running = False  

        screen.fill(BLACK)
        snake.draw(screen)
        pygame.display.flip()

        clock.tick(SNAKE_SPEED + snake.level)

    pygame.quit()

if __name__ == "__main__":
    main()
