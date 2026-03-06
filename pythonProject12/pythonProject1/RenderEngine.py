import pygame
import color
import consts


class RenderEngine:
    """
    Движок отрисовки, управляющий очередью рендеринга и отображением объектов на экране
    """

    def __init__(self):
        """
        Инициализация движка рендеринга
        """
        # Создание основного окна игры с заданными размерами
        self.surface = pygame.display.set_mode(consts.screen_params)
        # Установка заголовка окна
        pygame.display.set_caption(consts.game_title)
        # Очередь объектов для отрисовки
        self.render_queue = []

    def render(self):
        """
        Отрисовка всех объектов из очереди на экране
        """
        # Заливка всего экрана зеленым цветом (фон)
        self.surface.fill(color.green)

        # Перебор всех объектов в очереди и их отрисовка
        for render_object in self.render_queue:
            render_object.draw(self.surface)

        # Обновление содержимого экрана
        pygame.display.update()

        # Очистка очереди после отрисовки
        self.render_queue.clear()

    def add_render_object(self, *renders_object):
        """
        Добавление объектов в очередь на отрисовку

        Args:
            *renders_object: переменное количество объектов для отрисовки
        """
        for render_object in renders_object:
            self.render_queue.append(render_object)