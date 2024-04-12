import random  # Импорт модуля random для генерации случайных чисел
import pygame  # Импорт модуля pygame для создания игры

pygame.init()  # Инициализация Pygame

# Установка размеров окна
WIDTH, HEIGHT = 400, 600  
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание экрана

# Определение цветов в формате RGB
RED = (255, 0, 0)  
BLACK = (0, 0, 0)  
BLUE = (0, 0, 255)  
GREEN = (0, 255, 0)  
WHITE = (255, 255, 255)  

BLOCK_SIZE = 40  # Размер блока
SCORE = 0  # Начальный счет
clock = pygame.time.Clock()  # Создание объекта Clock для управления FPS
background = pygame.image.load('C:/Visual Studio Code/PP2/PP2/PP2/lab8/materials/AnimatedStreet.png')  # Загрузка фонового изображения
score_font = pygame.font.SysFont("Verdana", 30)  # Создание шрифта для отображения счета

# Класс Enemy - представляет вражеский объект
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10  # Скорость движения врага
        self.image = pygame.image.load('C:/Visual Studio Code/PP2/PP2/PP2/lab8/materials/Enemy.png')  # Загрузка изображения врага
        self.rect = self.image.get_rect()  # Получение прямоугольника, ограничивающего изображение
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )  # Установка начальной позиции врага

    def draw(self, surface):  # Метод для отрисовки врага на экране
        surface.blit(self.image, self.rect)

    def update(self):  # Метод для обновления состояния врага
        global SCORE  # Объявление глобальной переменной SCORE
        self.rect.move_ip(0, self.speed)  # Движение врага вниз
        if self.rect.y > HEIGHT:  # Если враг достиг нижней границы экрана
            SCORE += 1  # Увеличение счета
            self.speed += 1  # Увеличение скорости движения
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )  # Перемещение врага в случайное место вверху экрана

# Класс Player - представляет игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5  # Скорость движения игрока
        self.image = pygame.image.load('C:/Visual Studio Code/PP2/PP2/PP2/lab8/materials/Player.png')  # Загрузка изображения игрока
        self.rect = self.image.get_rect()  # Получение прямоугольника, ограничивающего изображение
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)  # Установка начальной позиции игрока

    def draw(self, surface):  # Метод для отрисовки игрока на экране
        surface.blit(self.image, self.rect)

    def update(self):  # Метод для обновления состояния игрока
        pressed = pygame.key.get_pressed()  # Получение состояния клавиш
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:  # Если нажата клавиша влево и игрок не выходит за границы экрана
            self.rect.move_ip(-self.speed, 0)  # Движение игрока влево
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:  # Если нажата клавиша вправо и игрок не выходит за границы экрана
            self.rect.move_ip(self.speed, 0)  # Движение игрока вправо

# Класс Coin - представляет монетку
class Coin(pygame.sprite.Sprite):
    def __init__(self, enemy_speed):
        super().__init__()
        self.speed = enemy_speed  # Скорость монетки
        self.image = pygame.image.load('C:/Visual Studio Code/PP2/PP2/PP2/lab8/materials/coin.png')  # Загрузка изображения монетки
        self.rect = self.image.get_rect()  # Получение прямоугольника, ограничивающего изображение
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            random.randint(self.rect.height, HEIGHT - self.rect.height),
        )  # Установка начальной позиции монетки

    def draw(self, surface):  # Метод для отрисовки монетки на экране
        surface.blit(self.image, self.rect)

    def update(self):  # Метод для обновления состояния монетки
        # Движение монетки
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
            self.rect.centerx = random.randint(0, WIDTH)

def main():  # Основная функция игры
    global SCORE  # Объявление глобальной переменной SCORE
    running = True  # Флаг работы игры
    player = Player()  # Создание объекта игрока
    enemy = Enemy()  # Создание объекта врага
    coin = Coin(enemy.speed)  # Создание объекта монетки
    enemies = pygame.sprite.Group()  # Группа врагов
    coins = pygame.sprite.GroupSingle()  # Группа с монеткой
    enemies.add(enemy)  # Добавление врага в группу
    coins.add(coin)  # Добавление монетки в группу

    while running:  # Главный игровой цикл
        SCREEN.blit(background, (0, 0))  # Отображение фонового изображения
        score = score_font.render(f" Your score: {SCORE}", True, (0, 0, 0))  # Создание изображения с текущим счетом
        SCREEN.blit(score, (0, 0))  # Отображение счета на экране

        for event in pygame.event.get():  # Обработка событий
            if event.type == pygame.QUIT:  # Если нажата кнопка закрытия окна
                running = False  # Завершение игры

        player.update()  # Обновление состояния игрока
        enemy.update()  # Обновление состояния врага
        coin.update()  # Обновление состояния монетки

        player.draw(SCREEN)  # Отрисовка игрока на экране
        enemy.draw(SCREEN)  # Отрисовка врага на экране
        coin.draw(SCREEN)  # Отрисовка монетки на экране

        if pygame.sprite.spritecollide(player, coins, dokill=True):  # Если игрок подобрал монетку
            SCORE += 5  # Увеличение счета на 5
            coin = Coin(enemy.speed)  # Создаем новую монетку
            coins.add(coin)  # Добавляем ее в группу монеток

        if pygame.sprite.spritecollideany(player, enemies):  # Если игрок столкнулся с врагом
            running = False  # Завершение игры

        pygame.display.flip()  # Обновление экрана
        clock.tick(60)  # Установка FPS

if __name__ == '__main__':
    main()  # Запуск основной функции игры
