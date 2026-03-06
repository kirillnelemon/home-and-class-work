import pygame
import copy
from CollidableObject import CollidableObject
from RenderObject import RenderObject


class Snake(CollidableObject, RenderObject):
    """
    Класс змейки, управляемой игроком
    """

    def __init__(self, color, block_size):
        """
        Инициализация змейки

        Args:
            color: цвет змейки
            block_size: размер одного блока змейки
        """
        self.color = color
        self.block_size = block_size
        # Список сегментов змейки
        self.snake_list = []
        # Длина змейки
        self.snake_length = 1
        # Вектор движения по X
        self.vector_x = 0
        # Вектор движения по Y
        self.vector_y = 0
        # Скорость движения
        self.speed = 10
        # Начальная позиция головы змейки
        self.head = pygame.Rect(200, 200, 10, 10)

    def move(self, x_change, y_change):
        """
        Изменение направления движения змейки

        Args:
            x_change: изменение по оси X
            y_change: изменение по оси Y
        """
        self.vector_x = x_change
        self.vector_y = y_change

    def update(self):
        """
        Обновление позиции змейки
        """
        # Перемещение головы
        self.head.x += self.vector_x
        self.head.y += self.vector_y
        # Обновление прямоугольника для коллизий
        self.rect = self.head
        # Добавление новой позиции головы в список сегментов
        self.snake_list.append(copy.copy(self.head))
        # Удаление лишних сегментов (если змейка не выросла)
        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]

    def draw(self, surface):
        """
        Отрисовка всех сегментов змейки

        Args:
            surface: поверхность для отрисовки
        """
        for part in self.snake_list:
            pygame.draw.rect(surface, self.color, part)

    def eat(self):
        """
        Увеличение длины змейки при поедании фрукта
        """
        self.snake_length += 1