import random
import pygame
import sqlite3

# Pygame initialization
pygame.init()

# Game window dimensions
WIDTH, HEIGHT = 600, 400

# Cell size in the game grid
CELL_SIZE = 20

# Initial snake speed
SNAKE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Connect to the database
conn = sqlite3.connect('snake_game.db')
cursor = conn.cursor()

# Create tables if not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS User (
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS User_Score (
    score_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    score INTEGER,
    level INTEGER,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);
""")
conn.commit()

class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.level = 1
        self.food = self.generate_food()
        self.food_timer = 10 * SNAKE_SPEED

    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction
        new_head = ((x + dx * CELL_SIZE) % WIDTH, (y + dy * CELL_SIZE) % HEIGHT)

        if new_head in self.body[1:] or (new_head[0] < 0 or new_head[0] > WIDTH or new_head[1] < 0 or new_head[1] > HEIGHT):
            return False

        self.body.insert(0, new_head)

        if new_head == self.food:
            self.score += random.randint(1, 3)
            if self.score % 3 == 0:
                self.level += 1
            self.food = self.generate_food()
            self.food_timer = 10 * SNAKE_SPEED
        else:
            self.body.pop()
            self.food_timer -= 1
            if self.food_timer == 0:
                self.food = self.generate_food()
                self.food_timer = 10 * SNAKE_SPEED
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

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(surface, RED, (self.food[0], self.food[1], CELL_SIZE, CELL_SIZE))

def display_text(surface, text, size, color, position):
    font = pygame.font.SysFont("Arial", size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

def authenticate_user(username):
    cursor.execute("SELECT user_id, username FROM User WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user:
        cursor.execute("SELECT level FROM User_Score WHERE user_id = ? ORDER BY score_id DESC LIMIT 1", (user[0],))
        level = cursor.fetchone()
        if level:
            return user[0], user[1], level[0]
        else:
            return user[0], user[1], 1
    else:
        return None

def create_user(username):
    cursor.execute("INSERT INTO User (username) VALUES (?)", (username,))
    conn.commit()
    return cursor.lastrowid

def save_game_state(user_id, score, level):
    cursor.execute("INSERT INTO User_Score (user_id, score, level) VALUES (?, ?, ?)", (user_id, score, level))
    conn.commit()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()

    username = input("Enter your username: ")
    user_info = authenticate_user(username)
    if user_info:
        user_id, username, level = user_info
    else:
        user_id = create_user(username)
        level = 1

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
                elif event.key == pygame.K_p:  # Pause and save game state
                    save_game_state(user_id, snake.score, snake.level)
                    running = False

        if not snake.move():
            running = False
        screen.fill(BLACK)
        snake.draw(screen)
        display_text(screen, f"Score: {snake.score}", 20, WHITE, (10, 10))
        display_text(screen, f"Level: {snake.level}", 20, WHITE, (10, 30))
        pygame.display.flip()
        clock.tick(SNAKE_SPEED + snake.level)

    pygame.quit()

if __name__ == "__main__":
    main()
