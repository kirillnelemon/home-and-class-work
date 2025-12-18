# log.py

class Log:
    wins = 0
    losses = 0
    draws = 0

    def __init__(self, lvl, name):
        self.lvl = lvl
        message = f"{name}, - новый герой!"
        print(message)
        self.write_to_log(message)

    def damage(self, name, damage_value):
        message = f"{name} нанес {damage_value} урона"
        print(message)
        self.write_to_log(message)

    def victory_lvl(self):
        Log.wins += 1
        message = "Поздравляем! Уровень пройден!"
        print(message)
        self.write_to_log(message)

    def faild_lvl(self):  # Опечатка сохранена как в оригинале
        Log.losses += 1
        message = "GAME OVER\nИгра окончена, вы проиграли("
        print(message)
        self.write_to_log(message)

    @staticmethod
    def show_stats():
        print(f"\n Статистика: Победы: {Log.wins}, Поражения: {Log.losses}, Ничьи: {Log.draws}")

    def write_to_log(self, message):
        with open("log.txt", 'a', encoding='utf-8') as f:
            f.write(message + "\n")