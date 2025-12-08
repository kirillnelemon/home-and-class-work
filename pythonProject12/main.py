import sys
import random
from snailrace import Snail, run_race, display_results


def Menu():
    """
    Главное меню приложения "Бега улиток".
    """
    print("Добро пожаловать в 'Бега улиток'!")
    while True:
        try:
            num_snails = int(input(f"Введите количество улиток для участия (от 5 до {Snail.max_num_snails}): "))
            if 5 <= num_snails <= Snail.max_num_snails:
                break
            else:
                print(f"Пожалуйста, введите число в диапазоне от 5 до {Snail.max_num_snails}.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    snails_list = []
    for i in range(num_snails):
        while True:
            name = input(f"Введите имя для улитки #{i + 1} (до {Snail.max_name_length} символов): ").strip()
            if not name:
                print("Имя не может быть пустым.")
            elif len(name) > Snail.max_name_length:
                print(f"Имя слишком длинное. Максимальная длина: {Snail.max_name_length} символов.")
            else:
                snails_list.append(Snail(name))
                break

    # Запуск гонки
    winners = run_race(snails_list)

    # Отображение результатов
    display_results(winners)


if __name__ == "__main__":
    try:
        Menu()
    except KeyboardInterrupt:
        print("\nГонка прервана пользователем. Выход из программы.")
        sys.exit(0)


