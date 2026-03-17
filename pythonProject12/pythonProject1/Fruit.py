import pygame
import SoundController
import color
import consts
from CollidableObject import CollidableObject
from RenderObject import RenderObject
import random


class Fruit(CollidableObject, RenderObject):
    """
    Класс фрукта, который появляется в случайном месте и может быть съеден змейкой
    """

    def __init__(self):
        """
        Инициализация фрукта со случайными координатами
        """
        # Цвет фрукта
        self.color = (color.red)
        # Размеры фрукта
        self.width = 15
        self.height = 15
        # Случайные координаты появления (с учетом размеров фрукта)
        self.x = random.randint(0, consts.screen_width - self.width)
        self.y = random.randint(0, consts.screen_height - self.height)
        # Прямоугольник для обработки столкновений
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        """
        Отрисовка фрукта на экране

        Args:
            surface: поверхность для отрисовки
        """
        pygame.draw.rect(surface, self.color, self.rect)

    def destroy(self):
        """
        Уничтожение фрукта с проигрыванием звука поедания
        """
        SoundController.fruit_eat.play()
        del self