import pygame
import SoundController
import color
import consts
from Fruit import Fruit
from RenderEngine import RenderEngine
from Snake import Snake


class SnakeGame:
    """
    Основной класс игры, управляющий всей логикой
    """

    def __init__(self):
        """
        Инициализация игры
        """
        # Инициализация pygame
        pygame.init()
        # Запуск фоновой музыки в цикле (-1 означает бесконечное повторение)
        SoundController.main_music.play(-1)
        # Создание движка рендеринга
        self.render = RenderEngine()
        # Создание таймера для контроля FPS
        self.clock = pygame.time.Clock()
        # Создание шрифта для отображения текста
        self.font_style = pygame.font.SysFont(None, 35)
        # Флаг окончания игры
        self.game_over = False
        # Флаг закрытия игры
        self.game_close = False
        # Создание змейки
        self.snake = Snake(color.black, 10)
        # Фрукт (изначально отсутствует)
        self.fruit = None

    def event_handler(self):
        """
        Обработка событий ввода (клавиатура, закрытие окна)
        """
        for event in pygame.event.get():
            # Обработка закрытия окна
            if event.type == pygame.QUIT:
                self.game_over = True
            # Обработка нажатия клавиш
            elif event.type == pygame.KEYDOWN:
                # Движение влево
                if event.key == pygame.K_LEFT:
                    self.snake.move(-self.snake.speed, 0)
                # Движение вправо
                elif event.key == pygame.K_RIGHT:
                    self.snake.move(self.snake.speed, 0)
                # Движение вверх
                elif event.key == pygame.K_UP:
                    self.snake.move(0, -self.snake.speed)
                # Движение вниз
                elif event.key == pygame.K_DOWN:
                    self.snake.move(0, self.snake.speed)

    def game_logic(self):
        """
        Основная логика игры
        """
        # Создание фрукта, если его нет
        if self.fruit is None:
            self.fruit = Fruit()

        # Обработка событий
        self.event_handler()

        # Проверка столкновения змейки с фруктом
        if self.snake.collide(self.fruit):
            self.snake.eat()  # Увеличение длины змейки
            self.fruit.destroy()  # Уничтожение съеденного фрукта
            self.fruit = Fruit()  # Создание нового фрукта

        # Обновление позиции змейки
        self.snake.update()

        # Проверка столкновения с границами экрана
        if self.snake.collide_with_screen_border():
            self.game_over = True  # Игра заканчивается при столкновении

        # Контроль FPS
        self.clock.tick(consts.game_FPS)

    def game_loop(self):
        """
        Главный игровой цикл
        """
        while not self.game_over:
            # Выполнение игровой логики
            self.game_logic()
            # Добавление объектов в очередь отрисовки
            self.render.add_render_object(self.fruit, self.snake)
            # Отрисовка всех объектов
            self.render.render()

        # Завершение игры
        pygame.quit()
        quit()