# Hero.py

'''
Структура персонажа (комментарии для разработки)
1) Уровень, имя, прозвище, происхождение
2) Принадлежность, возраст, здоровье, пол?
3) Умения и способности (список, словаря)
4) Слабые стороны персонажа
5) Радиус поражения/атака

Атрибуты персонажа:
1) Скорость
2) Интеллект
3) Сила
4) Ловкость
5) Удача
6) Сила атаки

Функции класса:
1) Атака, защита - базовые способности
2) Техники - механика игры
3) Способности - зависят от выбранного класса
'''

class Hero:
    def __init__(self, name, last_name, lor, history, hp, old, spells, radius, weaknesses,
                 speed, intelligence, power, lucky, agility, power_damage, exp):
        self.lvl = 1  # Уровень
        self.name = name  # Имя
        self.last_name = last_name  # Прозвище
        self.lor = lor  # Происхождение
        self.history = history  # Принадлежность
        self.hp = hp  # Здоровье
        self.old = old  # Возраст
        self.spells = spells  # Список способностей
        self.radius = radius  # Дальность атаки
        self.weaknesses = weaknesses  # Список слабостей
        self.attr = {
            "speed": speed,  # Скорость
            "intelligence": intelligence,  # Интеллект
            "power": power,  # Сила
            "lucky": lucky,  # Удача
            "agility": agility,  # Ловкость
            "power damage": power_damage  # Сила атаки
        }

    def attack_to_damage(self):
        # Атака персонажа
        pass

    def protection_to_damage(self):
        # Защита от урона
        pass