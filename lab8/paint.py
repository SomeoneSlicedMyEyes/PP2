import pygame

pygame.init()  # Инициализация Pygame
WIDTH, HEIGHT = 800, 800  # Установка ширины и высоты окна
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание экрана
BLACK = pygame.Color(0, 0, 0)  # Определение цветов
WHITE = pygame.Color(255, 255, 255)


class GameObject:
    def draw(self):  # Метод отрисовки
        raise NotImplementedError

    def handle(self, mouse_pos):  # Метод обработки событий
        raise NotImplementedError


class Button:
    def __init__(self):
        self.rect = pygame.draw.rect(  # Создание кнопки в виде прямоугольника
            SCREEN,
            (0, 255, 0),  # Цвет кнопки
            (WIDTH // 2 - 20, 20, 40, 40)  # Позиция и размеры кнопки
        )

    def draw(self):  # Метод отрисовки кнопки
        self.rect = pygame.draw.rect(
            SCREEN,
            (0, 255, 0),  # Цвет кнопки
            (WIDTH // 2 - 20, 20, 40, 40)  # Позиция и размеры кнопки
        )


class Pen(GameObject):
    def __init__(self, *args, **kwargs):
        self.points = []  # Список точек для рисования линии

    def draw(self):  # Метод отрисовки
        for idx, value in enumerate(self.points[:-1]):
            pygame.draw.line(
                SCREEN,
                WHITE,
                start_pos=value,  # Начальная позиция линии
                end_pos=self.points[idx + 1],  # Конечная позиция линии
            )

    def handle(self, mouse_pos):  # Метод обработки движения мыши
        self.points.append(mouse_pos)


class Rectangle(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos  # Начальная позиция прямоугольника
        self.end_pos = start_pos  # Конечная позиция прямоугольника

    def draw(self):  # Метод отрисовки прямоугольника
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.rect(
            SCREEN,
            WHITE,
            (
                start_pos_x,
                start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,  # Толщина линии
        )

    def handle(self, mouse_pos):  # Метод обработки движения мыши
        self.end_pos = mouse_pos


def main():  # Основная функция
    running = True  # Флаг работы игры
    clock = pygame.time.Clock()  # Создание объекта для отслеживания времени
    active_obj = None  # Активный объект (используется для рисования)
    button = Button()  # Создание кнопки

    objects = [
        button,  # Список объектов (в данном случае - кнопка)
    ]
    # current_shape = 'pen'
    current_shape = Pen  # Текущий инструмент рисования

    while running:  # Главный игровой цикл
        SCREEN.fill(BLACK)  # Заливка экрана черным цветом

        for event in pygame.event.get():  # Обработка событий
            if event.type == pygame.QUIT:  # Если нажата кнопка закрытия окна
                running = False  # Остановка игры

            if event.type == pygame.MOUSEBUTTONDOWN:  # Если нажата кнопка мыши
                if button.rect.collidepoint(event.pos):  # Если нажата кнопка
                    current_shape = Rectangle  # Текущий инструмент рисования - прямоугольник
                else:
                    active_obj = current_shape(start_pos=event.pos)  # Создание активного объекта

            if event.type == pygame.MOUSEMOTION and active_obj is not None:  # Если движение мыши и активный объект существует
                active_obj.handle(pygame.mouse.get_pos())  # Обработка движения мыши
                active_obj.draw()  # Отрисовка объекта

            if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:  # Если кнопка мыши отпущена и активный объект существует
                objects.append(active_obj)  # Добавление объекта в список
                active_obj = None  # Сброс активного объекта

        for obj in objects:  # Отрисовка всех объектов
            obj.draw()

        clock.tick(30)  # Установка FPS
        pygame.display.flip()  # Обновление экрана


if __name__ == '__main__':
    main()  # Запуск основной функции
