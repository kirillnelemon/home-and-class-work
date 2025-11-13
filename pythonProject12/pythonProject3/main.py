#Задание 1
def task1_directory():
    users_data = [
        [103, "555-1234"],
        [101, "555-9876"],
        [105, "555-4321"],
        [102, "555-6789"],
        [104, "555-5555"]
    ]

    print("\n--- Программа 'Справочник' ---")

    while True:
        print("\nВыберите действие:")
        print("1. Отсортировать по идентификационным кодам")
        print("2. Отсортировать по номерам телефона")
        print("3. Вывести список пользователей")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            users_data.sort(key=lambda user: user[0])
            print("Список отсортирован по идентификационным кодам.")
        elif choice == '2':
            users_data.sort(key=lambda user: user[1])
            print("Список отсортирован по номерам телефона.")
        elif choice == '3':
            if not users_data:
                print("Список пользователей пуст.")
            else:
                print("\n--- Текущий список пользователей ---")
                for user in users_data:
                    print(f"Код: {user[0]}, Телефон: {user[1]}")
        elif choice == '4':
            print("Выход из программы 'Справочник'.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие от 1 до 4.")
#Задание 2

def task2_books():
    books_data = [
        ["Python Crash Course", 2019],
        ["Automate the Boring Stuff with Python", 2015],
        ["Clean Code", 2008],
        ["The Hitchhiker's Guide to the Galaxy", 1979],
        ["Learning Python", 2013],
        ["Eloquent JavaScript", 2018]
    ]

    print("\n--- Программа 'Книги' ---")

    while True:
        print("\nВыберите действие:")
        print("1. Отсортировать по названию книг")
        print("2. Отсортировать по годам выпуска")
        print("3. Вывести список книг")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            books_data.sort(key=lambda book: book[0])
            print("Список книг отсортирован по названию.")
        elif choice == '2':
            books_data.sort(key=lambda book: book[1])
            print("Список книг отсортирован по годам выпуска.")
        elif choice == '3':
            if not books_data:
                print("Каталог книг пуст.")
            else:
                print("\n--- Текущий список книг ---")
                for book in books_data:
                    print(f"Название: '{book[0]}', Год: {book[1]}")
        elif choice == '4':
            print("Выход из программы 'Книги'.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие от 1 до 4."