import pygame
import consts


class CollidableObject:
    """
    Абстрактный класс для объектов, поддерживающих обработку столкновений
    """
    # Координаты объекта
    x = 0
    y = 0
    # Размеры объекта
    height = 0
    width = 0
    # Прямоугольник для обработки столкновений (используется встроенный механизм pygame)
    rect = pygame.Rect(x, y, width, height)

    def collide(self, collide_object):
        """
        Проверка столкновения с другим объектом

        Args:
            collide_object: другой объект для проверки столкновения

        Returns:
            bool: True если объекты столкнулись, иначе False
        """
        return collide_object.rect.colliderect(self.rect)

    def collide_with_right_border(self):
        """
        Проверка столкновения с правой границей экрана

        Returns:
            bool: True если объект коснулся правой границы
        """
        return self.rect.x > consts.screen_width - self.width

    def collide_with_left_border(self):
        """
        Проверка столкновения с левой границей экрана

        Returns:
            bool: True если объект коснулся левой границы
        """
        return self.rect.x < 0

    def collide_with_bottom_border(self):
        """
        Проверка столкновения с нижней границей экрана

        Returns:
            bool: True если объект коснулся нижней границы
        """
        return self.rect.y > consts.screen_height

    def collide_with_top_border(self):
        """
        Проверка столкновения с верхней границей экрана

        Returns:
            bool: True если объект коснулся верхней границы
        """
        return self.rect.y < 0

    def collide_with_screen_border(self):
        """
        Проверка столкновения с любой границей экрана

        Returns:
            bool: True если объект коснулся любой границы экрана
        """
        return (self.collide_with_right_border() or
                self.collide_with_left_border() or
                self.collide_with_bottom_border() or
                self.collide_with_top_border())