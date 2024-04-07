import random  # Импортируем модуль random для генерации случайных чисел
import pygame  # Импортируем библиотеку pygame для разработки игр

# Инициализируем pygame
pygame.init()

# Задаем ширину и высоту игрового окна
WIDTH, HEIGHT = 600, 400

# Задаем размер ячейки в игровой сетке
CELL_SIZE = 20

# Задаем начальную скорость змеи
SNAKE_SPEED = 10

# Определяем константы цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Определяем константы направлений
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Определяем класс Snake
class Snake:
    def __init__(self):
        # Инициализируем тело змеи одним сегментом в центре экрана
        self.body = [(WIDTH // 2, HEIGHT // 2)]

        # Выбираем случайное начальное направление движения змеи
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

        # Инициализируем счет и уровень
        self.score = 0
        self.level = 1

        # Генерируем первую еду для змеи
        self.food = self.generate_food()

    # Метод для движения змеи
    def move(self):
        # Получаем координаты головы змеи
        x, y = self.body[0]

        # Получаем направление движения
        dx, dy = self.direction

        # Вычисляем новые координаты головы змеи
        new_head = ((x + dx * CELL_SIZE) % WIDTH, (y + dy * CELL_SIZE) % HEIGHT)

        # Проверяем столкновения с телом змеи или границами игрового поля
        if new_head in self.body[1:] or self.check_border_collision(new_head):
            return False  # Возвращаем False, если произошло столкновение

        # Вставляем новую голову змеи в начало ее тела
        self.body.insert(0, new_head)

        # Проверяем, съела ли змея еду
        if new_head == self.food:
            # Увеличиваем счет
            self.score += 1

            # Проверяем, достигла ли змея условного количества очков для увеличения уровня
            if self.score % 3 == 0:
                self.level += 1

            # Генерируем новую еду
            self.food = self.generate_food()
        else:
            # Если змея не съела еду, удаляем последний сегмент хвоста
            self.body.pop()

        return True  # Возвращаем True, если змея успешно переместилась

    # Метод для изменения направления змеи
    def change_direction(self, direction):
        # Предотвращаем разворот змеи на 180 градусов
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    # Метод для генерации новой еды
    def generate_food(self):
        while True:
            # Генерируем случайные координаты для новой еды
            food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                    random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

            # Убеждаемся, что еда не попадает на тело змеи
            if food not in self.body:
                return food

    # Метод для проверки столкновений с границами игрового поля
    def check_border_collision(self, position):
        return position[0] < 0 or position[0] >= WIDTH or position[1] < 0 or position[1] >= HEIGHT

    # Метод для отрисовки змеи и еды на экране
    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(surface, RED, (self.food[0], self.food[1], CELL_SIZE, CELL_SIZE))

# Функция для отображения текста на экране
def display_text(surface, text, size, color, position):
    #отрисовка текста
    font = pygame.font.SysFont("Arial", size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, position)

# Основная функция для запуска игры
def main():
    # Создаем игровое окно
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')  # Задаем заголовок окна

    clock = pygame.time.Clock()  # Создаем объект часов для управления частотой кадров игры

    snake = Snake()  # Создаем объект змеи

    running = True  # Переменная для управления игровым циклом
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Завершаем игру, если мы закрываем окно
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        # Перемещаем змею и проверяем столкновения
        if not snake.move():
            running = False  # Завершаем игру, если змея столкнулась с собой или с границами

        # Заливаем экран черным цветом
        screen.fill(BLACK)

        # Отрисовываем змею и еду на экране
        snake.draw(screen)

        # Отображаем счет и уровень на экране
        display_text(screen, f"score: {snake.score}", 20, WHITE, (10, 10))
        display_text(screen, f"level: {snake.level}", 20, WHITE, (10, 30))

        pygame.display.flip()  # Обновляем экран
        clock.tick(SNAKE_SPEED + snake.level)  # Управляем частотой кадров игры

    pygame.quit()  # Завершаем pygame после завершения игрового цикла

# Запускаем основную функцию, если скрипт запущен непосредственно
if __name__ == "__main__":
    main()
