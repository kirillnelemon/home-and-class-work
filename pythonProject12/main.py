class BasketballDatabase:
    def __init__(self):
        # Словарь для хранения данных: {ФИО: рост (см)}
        self.players = {}

    def add_player(self, fio, height):
        """Добавление нового игрока."""
        if fio not in self.players:
            self.players[fio] = height
            print(f"Игрок {fio} добавлен.")
        else:
            print(f"Ошибка: Игрок {fio} уже существует.")

    def delete_player(self, fio):
        """Удаление игрока."""
        if fio in self.players:
            del self.players[fio]
            print(f"Игрок {fio} удален.")
        else:
            print(f"Ошибка: Игрок {fio} не найден.")

    def search_player(self, fio):
        """Поиск игрока и вывод его роста."""
        if fio in self.players:
            print(f"Рост игрока {fio}: {self.players[fio]} см.")
            return self.players[fio]
        else:
            print(f"Ошибка: Игрок {fio} не найден.")
            return None

    def update_player_height(self, fio, new_height):
        """Замена (обновление) роста игрока."""
        if fio in self.players:
            self.players[fio] = new_height
            print(f"Рост игрока {fio} обновлен до {new_height} см.")
        else:
            print(f"Ошибка: Игрок {fio} не найден.")

# Пример использования:
# db = BasketballDatabase()
# db.add_player("Майкл Джордан", 198)
# db.search_player("Майкл Джордан")
# db.update_player_height("Майкл Джордан", 199)
# db.delete_player("Майкл Джордан")


class Translator:
    def __init__(self):
        # Словарь для хранения данных: {английское слово: французский перевод}
        self.dictionary = {}

    def add_word(self, english, french):
        """Добавление новой пары слов."""
        if english not in self.dictionary:
            self.dictionary[english] = french
            print(f"Слово '{english}' добавлено.")
        else:
            print(f"Ошибка: Слово '{english}' уже в словаре.")

    def delete_word(self, english):
        """Удаление слова."""
        if english in self.dictionary:
            del self.dictionary[english]
            print(f"Слово '{english}' удалено.")
        else:
            print(f"Ошибка: Слово '{english}' не найдено.")

    def search_word(self, english):
        """Поиск перевода."""
        if english in self.dictionary:
            print(f"Перевод слова '{english}': {self.dictionary[english]}")
            return self.dictionary[english]
        else:
            print(f"Ошибка: Слово '{english}' не найдено.")
            return None

    def update_word(self, english, new_french):
        """Замена (обновление) перевода."""
        if english in self.dictionary:
            self.dictionary[english] = new_french
            print(f"Перевод слова '{english}' обновлен.")
        else:
            print(f"Ошибка: Слово '{english}' не найдено.")

# Пример использования:
# vocab = Translator()
# vocab.add_word("hello", "bonjour")
# vocab.search_word("hello")
# vocab.update_word("hello", "salut")
# vocab.delete_word("hello")


class CompanyDirectory:
    def __init__(self):
        # Словарь для хранения данных: {ФИО: {детали сотрудника}}
        self.employees = {}

    def add_employee(self, fio, details):
        """Добавление нового сотрудника с деталями."""
        if fio not in self.employees:
            self.employees[fio] = details
            print(f"Сотрудник {fio} добавлен.")
        else:
            print(f"Ошибка: Сотрудник {fio} уже в базе.")

    def delete_employee(self, fio):
        """Удаление сотрудника."""
        if fio in self.employees:
            del self.employees[fio]
            print(f"Сотрудник {fio} удален.")
        else:
            print(f"Ошибка: Сотрудник {fio} не найден.")

    def search_employee(self, fio):
        """Поиск информации о сотруднике."""
        if fio in self.employees:
            print(f"Данные сотрудника {fio}: {self.employees[fio]}")
            return self.employees[fio]
        else:
            print(f"Ошибка: Сотрудник {fio} не найден.")
            return None

    def update_employee(self, fio, new_details):
        """Замена (обновление) всех данных сотрудника."""
        if fio in self.employees:
            self.employees[fio] = new_details
            print(f"Данные сотрудника {fio} обновлены.")
        else:
            print(f"Ошибка: Сотрудник {fio} не найден.")

# Пример использования:
# firm = CompanyDirectory()
# firm.add_employee("Иван Петров", {"телефон": "123-456", "email": "ip@firm.com", "должность": "менеджер", "кабинет": 101, "skype": "ivan_p"})
# firm.search_employee("Иван Петров")
# firm.update_employee("Иван Петров", {"телефон": "999-888", "email": "ip_new@firm.com", "должность": "старший менеджер", "кабинет": 102, "skype": "ivan_p_new"})
# firm.delete_employee("Иван Петров")

class BookCollection:
    def __init__(self):
        # Словарь для хранения данных: {Название книги: {детали книги}}
        self.books = {}

    def add_book(self, title, details):
        """Добавление новой книги."""
        if title not in self.books:
            self.books[title] = details
            print(f"Книга '{title}' добавлена.")
        else:
            print(f"Ошибка: Книга '{title}' уже в коллекции.")

    def delete_book(self, title):
        """Удаление книги."""
        if title in self.books:
            del self.books[title]
            print(f"Книга '{title}' удалена.")
        else:
            print(f"Ошибка: Книга '{title}' не найдена.")

    def search_book(self, title):
        """Поиск информации о книге."""
        if title in self.books:
            print(f"Данные книги '{title}': {self.books[title]}")
            return self.books[title]
        else:
            print(f"Ошибка: Книга '{title}' не найдена.")
            return None

    def update_book(self, title, new_details):
        """Замена (обновление) данных о книге."""
        if title in self.books:
            self.books[title] = new_details
            print(f"Данные книги '{title}' обновлены.")
        else:
            print(f"Ошибка: Книга '{title}' не найдена.")

# Пример использования:
# library = BookCollection()
# library.add_book("1984", {"автор": "Джордж Оруэлл", "жанр": "Антиутопия", "год": 1949, "страниц": 328, "издательство": "Secker & Warburg"})
# library.search_book("1984")
# library.update_book("1984", {"автор": "Джордж Оруэлл", "жанр": "Классика", "год": 1949, "страниц": 328, "издательство": "Penguin"})
# library.delete_book("1984")
