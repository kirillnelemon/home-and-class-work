import os


def print_race(snails_list):
    """
    Отображает текущее состояние гонки с помощью ASCII-графики.
    """
    # Очистка экрана для плавного обновления (работает в консоли)
    os.system('cls' if os.name == 'nt' else 'clear')

    finish_line_pos = Snail.finish_line  # Должен импортировать класс Snail, но лучше передать

    print("\n" + "=" * (finish_line_pos + 10))
    print(f"|{'УЛИТОЧНЫЕ БЕГА':^{finish_line_pos + 8}}|")
    print("=" * (finish_line_pos + 10))
    print(f"| Статус: {'На трассе'.ljust(finish_line_pos + 6)} |")
    print("-" * (finish_line_pos + 10))

    for snail in snails_list:
        # ASCII-графика улитки: Раковина '@' и тело 'v'
        snail_ascii = "@vv"
        track_length = finish_line_pos

        # Определяем позицию улитки на треке
        pos = min(snail.position, track_length)

        # Формируем строку трека: пробелы + улитка + пробелы + финишная черта
        track = " " * pos + snail_ascii + " " * (track_length - pos) + "|"

        # Добавляем имя и статус
        name_status = f"{snail.name} ({snail.status})"
        print(f"| {track} {name_status.ljust(Snail.max_name_length + 10)}")

    print("-" * (finish_line_pos + 10))
    print(f"| START {' ' * (finish_line_pos - 5)} FINISH |")
    print("=" * (finish_line_pos + 10) + "\n")


# Импорт класса Snail нужен для доступа к константам
from snailrace import Snail
