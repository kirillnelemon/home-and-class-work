import random
import time
import sys
from print_race import print_race


class Snail:
    max_num_snails = 20
    max_name_length = 15
    finish_line = 40

    def __init__(self, name):
        self.name = name
        self.position = 0
        self.status = "Идет"  # Status can be "Идет", "Дрифт", "Спит", "Финиш"

    def drift(self):
        """Режим резкого повышения скорости (дрифт)."""
        speed_boost = random.randint(3, 7)
        self.position += speed_boost
        self.status = "Дрифт"
        # print(f"-> {self.name} вошел в ДРИФТ! Продвинулся на {speed_boost} позиций.")

    def move(self):
        """Обычное движение улитки."""
        speed = random.randint(1, 3)
        self.position += speed
        self.status = "Идет"

    def sleep(self):
        """Режим сна на трассе."""
        sleep_duration = random.randint(1, 3)
        self.status = f"Спит ({sleep_duration}с)"
        # print(f"-> {self.name} уснул на {sleep_duration} секунд.")
        time.sleep(0.5)  # Используем time.sleep(0.5) как базовый интервал

    def check_finish(self):
        """Проверяет, достигла ли улитка финиша."""
        return self.position >= self.finish_line


def run_race(snails_list):
    """
    Основной процесс гонки.
    """
    winners = []

    print("\nГОНКА НАЧИНАЕТСЯ!")
    time.sleep(1)

    while len(winners) < len(snails_list):
        for snail in snails_list:
            if snail.status == "Финиш":
                continue

            # Логика случайных событий: сон, дрифт или движение
            event_roll = random.randint(1, 10)
            if event_roll <= 2:
                snail.sleep()
            elif event_roll >= 9:
                snail.drift()
            else:
                snail.move()

            if snail.check_finish() and snail.status != "Финиш":
                snail.status = "Финиш"
                winners.append(snail)

        print_race(snails_list)
        time.sleep(0.5)  # Ожидание между шагами гонки

    return winners


def display_results(winners):
    """
    Отображение призеров (топ 3) и всех результатов.
    """
    print("\n" + "=" * 50)
    print("ГОНКА ОКОНЧЕНА! РЕЗУЛЬТАТЫ:")
    print("=" * 50)

    print("\n*** ТОП 3 ПРИЗЕРА ***")
    for i, winner in enumerate(winners[:3]):
        print(f"{i + 1} место: {winner.name} (Позиция: {winner.position})")

    print("\n*** ВСЕ УЧАСТНИКИ ГОНКИ ***")
    # Сортируем всех по финальной позиции для полного списка
    all_results = sorted(winners, key=lambda s: s.position, reverse=True)
    for i, snail in enumerate(all_results):
        print(f"Участник: {snail.name}, Финальная позиция: {snail.position}")

    print("=" * 50)

