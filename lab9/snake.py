import random  # Для генерации случайных чисел
import pygame  # Для создания игры

# Инициализация Pygame
pygame.init()

# Задаем размеры игрового окна
WIDTH, HEIGHT = 600, 400

# Размер ячейки в игровой сетке
CELL_SIZE = 20

# Начальная скорость змеи
SNAKE_SPEED = 10

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Определение направлений
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Класс, представляющий змею в игре
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]  # Тело змеи
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])  # Направление
        self.score = 0  # Счет
        self.level = 1  # Уровень
        self.food = self.generate_food()  # Еда для змеи
        self.food_timer = 10 * SNAKE_SPEED  # Таймер для исчезновения еды

    # Метод для движения змеи
    def move(self):
        x, y = self.body[0]  # Текущая позиция головы змеи
        dx, dy = self.direction  # Направление движения

        # Вычисление новой позиции головы змеи
        new_head = ((x + dx * CELL_SIZE) % WIDTH, (y + dy * CELL_SIZE) % HEIGHT)

        # Проверка на столкновения с телом или границами
        if new_head in self.body[1:] or (new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT):
            return False  # Змея столкнулась

        self.body.insert(0, new_head)  # Добавляем новую голову

        # Проверка съедания еды
        if new_head == self.food:
            self.score += random.randint(1, 3)  # Увеличение счета на 1-3
            if self.score % 3 == 0:
                self.level += 1  # Увеличение уровня каждые 3 очка
            self.food = self.generate_food()  # Создание новой еды
            self.food_timer = 10 * SNAKE_SPEED  # Сброс таймера
        else:
            self.body.pop()  # Удаление последнего сегмента хвоста
            self.food_timer -= 1  # Уменьшение таймера
            if self.food_timer == 0:
                self.food = self.generate_food()  # Пересоздание еды
                self.food_timer = 10 * SNAKE_SPEED  # Сброс таймера
        return True  # Змея двигается

    # Метод для изменения направления змеи
    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction  # Изменение направления

    # Метод для генерации новой еды
    def generate_food(self):
        while True:
            food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                    random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
            if food not in self.body:
                return food  # Создание еды

    # Метод для отрисовки змеи и еды на экране
    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(surface, RED, (self.food[0], self.food[1], CELL_SIZE, CELL_SIZE))

# Функция для отображения текста на экране
def display_text(surface, text, size, color, position):
    font = pygame.font.SysFont("Arial", size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

# Основная функция для запуска игры
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание игрового окна
    pygame.display.set_caption('Snake Game')  # Установка заголовка окна

    clock = pygame.time.Clock()  # Создание часов для управления частотой кадров

    snake = Snake()  # Создание объекта змеи

    running = True  # Переменная для управления циклом игры
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Завершение игры при закрытии окна
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
            running = False  # Завершение игры при столкновении

        screen.fill(BLACK)  # Заливка экрана черным цветом
        snake.draw(screen)  # Отрисовка змеи и еды
        display_text(screen, f"Score: {snake.score}", 20, WHITE, (10, 10))  # Отображение счета
        display_text(screen, f"Level: {snake.level}", 20, WHITE, (10, 30))  # Отображение уровня
        pygame.display.flip()  # Обновление экрана
        clock.tick(SNAKE_SPEED + snake.level)  # Управление частотой кадров

    pygame.quit()  # Завершение Pygame после завершения игрового цикла

# Запуск основной функции, если скрипт запущен непосредственно
if __name__ == "__main__":
    main()
