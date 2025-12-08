#
# #практика 1
# # задание 1
# import random
# import math
#
#
# class Number:
#     def __init__(self, size, min_val, max_val):
#         self.data = [random.randint(min_val, max_val) for _ in range(size)]
#         self.size = size
#         print(f"Исходный список: {self.data}")
#
#     def process_list(self):
#         if not self.data:
#             print("Список пуст, обработка невозможна.")
#             return
#
#         average = sum(self.data) / len(self.data)
#         print(f"Среднее арифметическое: {average:.2f}")
#
#         n = self.size
#
#         end_sorted_index = math.floor(2 * n / 3) if average > 0 else math.floor(n / 3)
#         start_reversed_index = end_sorted_index
#
#         part_to_sort = self.data[:end_sorted_index]
#         part_to_reverse = self.data[start_reversed_index:]
#
#         part_to_sort.sort()
#
#         part_to_reverse.reverse()
#
#         self.data = part_to_sort + part_to_reverse
#
#         print(f"Обработанный список: {self.data}")
#
# #задание 2
# def display_grades(grades):
#     print(f"Текущие оценки: {grades}")
#
#
# def retake_exam(grades):
#     try:
#         item_number = int(input("Введите номер элемента списка для изменения (от 1 до 10): "))
#         if not (1 <= item_number <= 10):
#             print("Некорректный номер элемента.")
#             return
#
#         new_grade = int(input("Введите новую оценку (от 1 до 12): "))
#         if not (1 <= new_grade <= 12):
#             print("Оценка должна быть от 1 до 12.")
#             return
#
#         # Обновляем оценку (item_number - 1, т.к. индексы с 0)
#         grades[item_number - 1] = new_grade
#         print("Оценка успешно обновлена.")
#     except ValueError:
#         print("Некорректный ввод. Введите целое число.")
#
#
# def check_scholarship(grades):
#
#     if not grades:
#         print("Список оценок пуст.")
#         return
#
#     average = sum(grades) / len(grades)
#     print(f"Средний балл: {average:.2f}")
#
#     if average >= 10.7:
#         print("Стипендия **выходит**.")
#     else:
#         print("Стипендия **не выходит**.")
#
#
# def display_sorted_grades(grades):
#
#     sort_choice = input("Выберите порядок сортировки (1 - возрастание, 2 - убывание): ")
#     sorted_grades = sorted(grades)
#
#     if sort_choice == '1':
#         print(f"Оценки по возрастанию: {sorted_grades}")
#     elif sort_choice == '2':
#         sorted_grades.reverse()
#         print(f"Оценки по убыванию: {sorted_grades}")
#     else:
#         print("Неверный выбор порядка сортировки.")
#
#
# def main():
#
#     grades = []
#     while len(grades) < 10:
#         try:
#             grade = int(input(f"Введите оценку {len(grades) + 1} из 10 (от 1 до 12): "))
#             if 1 <= grade <= 12:
#                 grades.append(grade)
#             else:
#                 print("Оценка должна быть от 1 до 12.")
#         except ValueError:
#             print("Некорректный ввод. Введите целое число.")
#
#     while True:
#         print("\n--- Меню ---")
#         print("1. Вывод оценок")
#         print("2. Пересдача экзамена (изменить оценку)")
#         print("3. Выходит ли стипендия")
#         print("4. Вывод отсортированного списка оценок")
#         print("5. Выход")
#
#         choice = input("Выберите пункт меню: ")
#
#         if choice == '1':
#             display_grades(grades)
#         elif choice == '2':
#             retake_exam(grades)
#         elif choice == '3':
#             check_scholarship(grades)
#         elif choice == '4':
#             display_sorted_grades(grades)
#         elif choice == '5':
#             print("Выход из программы.")
#             break
#         else:
#             print("Неверный выбор, попробуйте снова.")
#
#
#
# if __name__ == "__main__":
#     main()
# #задание 3
# def bubble_sort_improved(arr):
#     n = len(arr)
#
#     for i in range(n):
#
#         swapped = False
#
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 # Обмен элементов
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#
#         if not swapped:
#             print(f"Сортировка завершена досрочно на шаге {i + 1}, перестановок нет.")
#             break
#         else:
#             print(f"Шаг {i + 1}: произведены перестановки.")
#
#     return arr
#
# #практика 2
# #задание 1
# import sys
#
# def display_users(codes, phones):
#     if not codes:
#         print("Список пользователей пуст.")
#         return
#     print("\n--- Список пользователей ---")
#     print(f"{'Код':<15} | {'Телефон':<15}")
#     print("-" * 33)
#     for code, phone in zip(codes, phones):
#         print(f"{code:<15} | {phone:<15}")
#
# def add_user(codes, phones):
#     try:
#         code = int(input("Введите идентификационный код (целое число): "))
#         phone = int(input("Введите телефонный номер (целое число): "))
#         codes.append(code)
#         phones.append(phone)
#         print("Пользователь добавлен.")
#     except ValueError:
#         print("Некорректный ввод. Ожидаются целые числа.")
# #задание 2
# import sys
#
# def display_books(titles, years):
#
#     if not titles:
#         print("Список книг пуст.")
#         return
#     print("\n--- Список книг ---")
#     print(f"{'Название':<30} | {'Год выпуска':<15}")
#     print("-" * 47)
#
#     for title, year in zip(titles, years):
#         print(f"{title:<30} | {year:<15}")
#
# def add_book(titles, years):
#     try:
#         title = input("Введите название книги: ")
#         year = int(input("Введите год выпуска: "))
#         if not title:
#             print("Название не может быть пустым.")
#             return
#         if not (0 < year < 2100):
#              print("Некорректный год.")
#              return
#         titles.append(title)
#         years.append(year)
#         print("Книга добавлена.")
#     except ValueError:
#         print("Некорректный ввод. Ожидается целое число для года.")
# #практика 3
# #задание 1
# def solve_task():
#     # Исходные четыре списка целых чисел
#     list1 = [12, 5, 8]
#     list2 = [45, 1, 99]
#     list3 = [3, 15, 6]
#     list4 = [22, 10, 78]
#
#     # Объединение списков в пятый
#     fifth_list = list1 + list2 + list3 + list4
#     print(f"Объединенный список: {fifth_list}")
#
#     # Выбор порядка сортировки пользователем
#     sort_choice = input("Выберите порядок сортировки (1 - возрастание, 2 - убывание): ")
#
#     if sort_choice == '1':
#         # Сортировка по возрастанию (по умолчанию)
#         fifth_list.sort()
#         print(f"Отсортированный список (возрастание): {fifth_list}")
#     elif sort_choice == '2':
#         # Сортировка по убыванию
#         fifth_list.sort(reverse=True)
#         print(f"Отсортированный список (убывание): {fifth_list}")
#     else:
#         print("Неверный выбор порядка сортировки. Список оставлен без изменений.")
#
#     return fifth_list
# #задание 2
# def find_overall_unique_elements(list1, list2, list3, list4):
#
#     all_elements = list1 + list2 + list3 + list4
#
#     from collections import Counter
#     counts = Counter(all_elements)
#
#     unique_elements = [item for item, count in counts.items() if count == 1]
#     return unique_elements
# #практика 4
# #задание 1
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# #задание 2
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#
#         arr[j + 1] = key
#     return arr
# #задание 3
# def sort_list_halves(arr):
#     n = len(arr)
#     mid_point = n // 2
#     first_half = arr[:mid_point]
#     second_half = arr[mid_point:]
#     first_half.sort(reverse=True)
#     second_half.sort()
#     arr[:mid_point] = first_half
#     arr[mid_point:] = second_half
#
#     return arr
# #задание 4
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         L = arr[:mid]
#         R = arr[mid:]
#         merge_sort(L)
#         merge_sort(R)
#         i = j = k = 0
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#     return arr
# #практика 5
# #задание 1
# def shell_sort(arr):
#     n = len(arr)
#     gap = n // 2
#     while gap > 0:
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i
#             while j >= gap and arr[j - gap] > temp:
#                 arr[j] = arr[j - gap]
#                 j -= gap
#
#             arr[j] = temp
#
#         gap //= 2
#     return arr
# #задание 2
# def heapify(arr, n, i):
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#     if l < n and arr[l] > arr[largest]:
#         largest = l
#     if r < n and arr[r] > arr[largest]:
#         largest = r
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#
#         heapify(arr, n, largest)
#
# #задание 3
# def partition(arr, low, high):
#     i = (low - 1)
#     pivot = arr[high]
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
# #задание 4
# def flip(arr, k):
#     left = 0
#     right = k - 1
#     while left < right:
#         arr[left], arr[right] = arr[right], arr[left]
#         left += 1
#         right -= 1
#
# def pancake_sort(arr):
#     n = len(arr)
#     for current_size in range(n, 1, -1):
#         max_idx = arr.index(max(arr[:current_size]))
#         if max_idx != current_size - 1:
#             flip(arr, max_idx + 1)
#             flip(arr, current_size)
#     return arr
# #практика 6
# #задание 1
# def linear_search(arr, target):
#     for index, value in enumerate(arr):
#         if value == target:
#             return index
#     return -1
# import random
# def main():
#     my_list = [random.randint(1, 100) for _ in range(10)]
#     print(f"Сгенерированный список: {my_list}")
#
#     try:
#         search_value = int(input("Введите целое число для поиска: "))
#
#         found_index = linear_search(my_list, search_value)
#
#         if found_index != -1:
#             print(f"Число {search_value} найдено в списке по индексу **{found_index}**.")
#         else:
#             print(f"Число {search_value} не найдено в списке.")
#
#     except ValueError:
#         print("Некорректный ввод. Пожалуйста, введите целое число.")
#
# if __name__ == "__main__":
#     main()
# #задание 2
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
#
#
# import random
#
#
# def main():
#     my_list = [random.randint(1, 100) for _ in range(10)]
#     print(f"Сгенерированный список: {my_list}")
#     my_list.sort()
#     print(f"Отсортированный список: {my_list}")
#     try:
#         search_value = int(input("Введите целое число для поиска: "))
#         found_index = binary_search(my_list, search_value)
#         if found_index != -1:
#             print(f"Число {search_value} найдено в списке по индексу **{found_index}**.")
#         else:
#             print(f"Число {search_value} не найдено в списке.")
#
#     except ValueError:
#         print("Некорректный ввод. Пожалуйста, введите целое число.")
# if __name__ == "__main__":
#     main()
# #задание 3
# class Soda:
#     def __init__(self, additive=None):
#         self.additive = additive
#
#     def display_drink(self):
#         if self.additive:
#             return f"Газированная вода со вкусом {self.additive}."
#         else:
#             return "Обычная газированная вода (без добавок)."
#         # Пример использования класса:
#
#         # 1. Создание лимонада с добавкой
#         lemonade_cherry = Soda("вишни")
#         print(lemonade_cherry.display_drink())
#
#         # 2. Создание обычной газированной воды (без добавки)
#         soda_plain = Soda()
#         print(soda_plain.display_drink())
#
#         # 3. Пример с другой добавкой
#         lemonade_orange = Soda("апельсина")
#         print(lemonade_orange.display_drink())
# #задание 4
# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if not (isinstance(self.a, (int, float)) and
#                 isinstance(self.b, (int, float)) and
#                 isinstance(self.c, (int, float))):
#             return "Нужно вводить только числа!;"
#         if self.a <= 0 or self.b <= 0 or self.c <= 0:
#             return "С отрицательными числами ничего не выйдет!;"
#         if (self.a + self.b > self.c and
#             self.a + self.c > self.b and
#             self.b + self.c > self.a):
#             return "Ура, можно построить треугольник!;"
#         else:
#             return "Жаль, но из этого треугольник не сделать."
# # Примеры использования и тестирование
#
# # 1. Корректный треугольник (сумма двух сторон больше третьей: 3+4 > 5)
# t1 = TriangleChecker(3, 4, 5)
# print(f"Тест 1 (корректные стороны): {t1.is_triangle()}")
#
# # 2. Невозможно построить треугольник (3+4 не больше 7)
# t2 = TriangleChecker(3, 4, 7)
# print(f"Тест 2 (не треугольник): {t2.is_triangle()}")
#
# # 3. Отрицательные числа
# t3 = TriangleChecker(-1, 4, 5)
# print(f"Тест 3 (отрицательное число): {t3.is_triangle()}")
#
# # 4. Нечисловые данные (строка)
# t4 = TriangleChecker('a', 4, 5)
# print(f"Тест 4 (не число): {t4.is_triangle()}")
#
# # 5. Использование чисел с плавающей точкой
# t5 = TriangleChecker(2.5, 3.5, 4.0)
# print(f"Тест 5 (float числа): {t5.is_triangle()}")
# #задание 5
# class Nikola:
#     def __init__(self, name, age):
#         self.age = age
#         if name == "Николай":
#             self.name = "Николай"
#         else:
#             self.name = f"Я не {name}, а Николай"
#
#     def display_info(self):
#         print(f"Имя: {self.name}, Возраст: {self.age}")
# class Nikola:
#     def __init__(self, name, age):
#         self.age = age
#         if name == "Николай":
#             self.name = "Николай"
#         else:
#             self.name = f"Я не {name}, а Николай"
#
#     def display_info(self):
#         print(f"Имя: {self.name}, Возраст: {self.age}")
#     def __setattr__(self, name, value):
#         if 'name' in self.__dict__ or 'age' in self.__dict__:
#             # Проверяем, пытаются ли перезаписать существующие атрибуты
#             if name in self.__dict__:
#                 super().__setattr__(name, value)
#             else:
#                 print(f"Ошибка: Нельзя добавить новый атрибут '{name}' к экземпляру класса Nikola.")
#         else:
#             super().__setattr__(name, value)
# #ЗАДАНИЕ 6
# class Programmer:
#     RATES = {
#         "Junior": 10,
#         "Middle": 15,
#         "Senior": 20
#     }
#
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#         self.hours_worked = 0
#         self.salary_per_hour = self.RATES[position]
#         self.total_salary = 0
#
#
# class Programmer:
#     # ... (код из Step 1 остается прежним) ...
#     RATES = {
#         "Junior": 10,
#         "Middle": 15,
#         "Senior": 20
#     }
#
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#         self.hours_worked = 0
#         self.salary_per_hour = self.RATES[position]
#         self.total_salary = 0
#     def work(self, time):
#         if time > 0:
#             self.hours_worked += time
#             self.total_salary += time * self.salary_per_hour
#         else:
#             print("Время работы должно быть положительным числом.")
#     def rise(self):
#         if self.position == "Junior":
#             self.position = "Middle"
#             self.salary_per_hour = self.RATES["Middle"]
#         elif self.position == "Middle":
#             self.position = "Senior"
#             self.salary_per_hour = self.RATES["Senior"]
#         elif self.position == "Senior":
#             self.salary_per_hour += 1
#             print(f"Оклад повышен до {self.salary_per_hour} тгр/час.")
#         else:
#             self.salary_per_hour += 1
#
#         print(f"{self.name} повышен до должности {self.position} с окладом {self.salary_per_hour} тгр/час.")
#
#     def info(self):
#         return (f"{self.name} {self.hours_worked}ч.\n"
#                 f"{self.total_salary} тгр..")
# #задание 7
# import random
#
# # Базовый класс NPC
# class NPC:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#
#     def display_info(self):
#         """Выводит текущее состояние NPC."""
#         print(f"Имя: {self.name}, Очки здоровья: {self.health}")
#
#     def attack(self):
#         """Базовый метод атаки."""
#         return 0 # Базовый класс не наносит урона
#
# # Класс Swordsman (Мечник), наследует NPC
# class Swordsman(NPC):
#     def __init__(self, name, health, min_damage, max_damage):
#         super().__init__(name, health)
#         self.min_damage = min_damage
#         self.max_damage = max_damage
#
#     def attack(self):
#         """Наносит случайный урон из заданного диапазона."""
#         damage = random.randint(self.min_damage, self.max_damage)
#         return damage
#
# # Класс Mage (Маг), наследует NPC
# class Mage(NPC):
#     def __init__(self, name, health, mana):
#         super().__init__(name, health)
#         self.mana = mana
#
#     def attack(self):
#         if self.mana > 0:
#             damage = self.mana * 2
#             self.mana = 0
#             return damage
#         else:
#             return 0
# if __name__ == "__main__":
#
#     bilbo = NPC("Бильбо", 15)
#     gandalf = Mage("Гендальф", 100, 5) # Мана 5 => 10 урона
#     aragorn = Swordsman("Арагорн", 50, 5, 10) # Диапазон урона 5-10
#
#     print("--- Сценарий 1 ---")
#     bilbo.display_info()
#     print("Не могу атаковать!")
#
#     print("\n--- Сценарий 2 (Гендальф) ---")
#     gandalf.display_info()
#     damage_gandalf_1 = gandalf.attack()
#     if damage_gandalf_1 > 0:
#         print(f"Маг Гендальф нанёс **{damage_gandalf_1}** урона!")
#
#     print("\n--- Сценарий 3 (Арагорн) ---")
#     aragorn.display_info()
#     damage_aragorn = aragorn.attack()
#     if damage_aragorn > 0:
#         print(f"Мечник Арагорн нанёс **{damage_aragorn}** урона!")
#
#     print("\n--- Сценарий 4 (Гендальф повторно) ---")
#     gandalf.display_info()
#     damage_gandalf_2 = gandalf.attack()
#     if damage_gandalf_2 == 0:
#         print("Не могу атаковать! Мана закончилась.")
# #практика 7
# #задание 1
# class Animal:
#     def __init__(self, nickname):
#         self.nickname = nickname
#
#     def __str__(self):
#         return f"Животное с кличкой: {self.nickname}"
#
# class Cat(Animal):
#     def voice(self):
#         print("Мяу!")
#
#     def run(self):
#         print("Побежали!")
#
# class Parrot(Animal):
#     def voice(self):
#         print("Привет!")
#
#     def fly(self):
#         print("Полетели!")
#
# # Пример использования
# cat = Cat("Барсик")
# parrot = Parrot("Кеша")
#
# print(cat)
# cat.voice()
# cat.run()
#
# print(parrot)
# parrot.voice()
# parrot.fly()
# #задание 2
# class Message:
#     def __init__(self, sender, recipient):
#         self.sender = sender
#         self.recipient = recipient
#
#     def showHeader(self):
#         print(f"Отправитель: {self.sender}, Получатель: {self.recipient}")
#
# class TextMessage(Message):
#     def __init__(self, sender, recipient, text):
#         super().__init__(sender, recipient)
#         self.text = text
#
#     def send(self):
#         self.showHeader()
#         print(self.text)
#
# class StickerMessage(Message):
#     def __init__(self, sender, recipient, sticker):
#         super().__init__(sender, recipient)
#         self.sticker = sticker
#         self.count = 1
#
#     def send(self):
#         self.showHeader()
#         print(f"{self.sticker} {self.count}")
#         self.count += 1
#
# # Пример использования:
# text_msg = TextMessage("Алиса", "Боб", "Привет, как дела?")
# text_msg.send()
#
# print("-" * 20)
#
# sticker_msg = StickerMessage("Боб", "Алиса", "(¬_¬)")
# sticker_msg.send() # Count будет 1
# sticker_msg.send() # Count будет 2
# sticker_msg.send() # Count будет 3
# #ЗАДАНИЕ 3
# import random
#
# class MSDice:
#     def __init__(self, num_faces):
#         self.num_faces = num_faces
#         self.current_value = 0
#
#     def roll(self):
#         self.current_value = random.randint(1, self.num_faces)
#         return self.current_value
#
#     def __str__(self):
#         return f"D{self.num_faces} с текущим значением: {self.current_value}"
#
#     def __repr__(self):
#         return self.__str__()
#
# class D4(MSDice):
#     def __init__(self):
#         super().__init__(4)
#
# class D6(MSDice):
#     def __init__(self):
#         super().__init__(6)
#
# class D10(MSDice):
#     def __init__(self):
#         super().__init__(10)
#
# class D20(MSDice):
#     def __init__(self):
#         super().__init__(20)
#
# # Пример использования:
# d6_cube = D6()
# print(f"Кубик D6 до броска: {d6_cube}")
# d6_cube.roll()
# print(f"Кубик D6 после броска: {d6_cube}")
#
# d20_cube = D20()
# d20_cube.roll()
# print(f"Кубик D20 после броска: {d20_cube}")
# #задание 4
# class Player:
#     def __init__(self, nickname):
#         # Конструктор принимает имя игрока и инициализирует поля
#         self.nickname = nickname
#         self.exp_points = 0  # Начальное значение 0
#         self.inventory = []  # Начальное значение []
#
#     def __str__(self):
#         # Преобразование объекта в строку для вывода
#         return f"Игрок: {self.nickname}, Опыт: {self.exp_points}, Инвентарь: {', '.join(self.inventory)}"
#
#     def addExp(self, exp):
#         # Добавление очков опыта
#         if exp > 0:
#             self.exp_points += exp
#
#     def addItem(self, item):
#         # Добавление предмета в инвентарь (строка)
#         if item not in self.inventory:
#             self.inventory.append(item)
#
#     def removeItem(self, item):
#         # Удаление предмета из инвентаря
#         if item in self.inventory:
#             self.inventory.remove(item)
# # Создаем нового игрока
# player = Player("Геральт")
# print(player)
#
# # Добавляем опыт и предметы
# player.addExp(100)
# player.addItem("Меч")
# player.addItem("Зелье лечения")
# print(player)
#
# # Удаляем предмет
# player.removeItem("Зелье лечения")
# print(player)
# #ЗАДАНИЕ 5
# class resistors:
#     def parallel(self, r1, r2):
#         if (r1 + r2) == 0:
#             return 0
#         return (r1 * r2) / (r1 + r2)
# #практика 8
# #задание 1
# class SimpleStatistics:
#     def __init__(self, numbers_list):
#         # Принимает список чисел
#         self.numbers = sorted(numbers_list) # Сортируем для упрощения расчета медианы
#
#     def mean(self):
#         # Вычисление среднего арифметического
#         if not self.numbers:
#             return 0
#         return sum(self.numbers) / len(self.numbers)
#
#     def median(self):
#         # Вычисление медианы
#         n = len(self.numbers)
#         if n == 0:
#             return 0
#         if n % 2 == 1:
#             # Нечетное количество элементов - берем средний
#             return self.numbers[n // 2]
#         else:
#             # Четное количество элементов - среднее двух центральных
#             mid1 = self.numbers[n // 2 - 1]
#             mid2 = self.numbers[n // 2]
#             return (mid1 + mid2) / 2
#
#     def mode(self):
#         # Вычисление моды (возвращает список мод)
#         if not self.numbers:
#             return []
#         counts = {}
#         for num in self.numbers:
#             counts[num] = counts.get(num, 0) + 1
#         max_count = max(counts.values())
#         modes = [key for key, value in counts.items() if value == max_count]
#         return modes
#
#     def range_val(self):
#         # Вычисление размаха (максимальное - минимальное)
#         if not self.numbers:
#             return 0
#         return self.numbers[-1] - self.numbers[0]
#
#     def variance(self):
#         # Вычисление выборочной дисперсии
#         if len(self.numbers) < 2:
#             return 0
#         mean_val = self.mean()
#         # Сумма квадратов отклонений от среднего
#         sum_of_squares = sum([(x - mean_val) ** 2 for x in self.numbers])
#         # Делим на (n - 1) для выборочной дисперсии
#         return sum_of_squares / (len(self.numbers) - 1)
#
#     def standard_deviation(self):
#         # Вычисление выборочного стандартного отклонения
#         # Квадратный корень из дисперсии
#         return self.variance() ** 0.5
# data = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8]
# stats = SimpleStatistics(data)
#
# print(f"Список чисел: {data}")
# print(f"Среднее арифметическое (mean): {stats.mean()}")
# print(f"Медиана (median): {stats.median()}")
# print(f"Мода (mode): {stats.mode()}")
# print(f"Размах (range): {stats.range_val()}")
# print(f"Выборочная дисперсия (variance): {stats.variance()}")
# print(f"Выборочное стандартное отклонение (standard deviation): {stats.standard_deviation()}")
# #задание 2
# from collections import Counter
#
#
# class FrequencyDistribution:
#     def __init__(self, data_list):
#         self.data = data_list
#         self.frequencies = {}
#
#     def calculate_frequencies(self):
#         """Подсчет частоты каждого уникального элемента в данных."""
#         # Используем collections.Counter для простоты подсчета
#         self.frequencies = dict(Counter(self.data))
#         return self.frequencies
#
#     def display_frequency_table(self):
#         """Вывод таблицы частот в читаемом формате."""
#         if not self.frequencies:
#             print("Сначала рассчитайте частоты с помощью calculate_frequencies().")
#             return
#
#         print("--- Таблица частот ---")
#         print(f"| {'Элемент'.ljust(15)} | {'Частота'.ljust(8)} |")
#         print("-" * 30)
#         for item, frequency in self.frequencies.items():
#             print(f"| {str(item).ljust(15)} | {str(frequency).ljust(8)} |")
#         print("-" * 30)
#
#     def get_most_frequent(self):
#         """Возвращает элементы с наибольшей частотой."""
#         if not self.frequencies:
#             return []
#
#         max_freq = max(self.frequencies.values())
#         most_frequent_items = [item for item, freq in self.frequencies.items() if freq == max_freq]
#         return most_frequent_items
# # Пример нечисловых данных
# data = 1
# freq_dist = FrequencyDistribution(data)
#
# # 1. Расчет частот
# freq_dist.calculate_frequencies()
# print(f"Словарь частот: {freq_dist.frequencies}\n")
#
# # 2. Вывод таблицы частот
# freq_dist.display_frequency_table()
#
# # 3. Получение наиболее часто встречающихся элементов
# most_freq = freq_dist.get_most_frequent()
# print(f"\nНаиболее частые элементы: {most_freq}")
#
# #задание 3
# import math
# import matplotlib.pyplot as plt
#
#
# class Correlation:
#     def __init__(self, X, Y):
#         # Принимает два списка чисел X и Y одинаковой длины
#         if len(X) != len(Y):
#             raise ValueError("Списки X и Y должны быть одинаковой длины")
#         self.X = X
#         self.Y = Y
#         self.n = len(X)
#
#     def _mean(self, data):
#         # Вспомогательный метод для расчета среднего значения
#         if self.n == 0:
#             return 0
#         return sum(data) / self.n
#
#     def covariance(self):
#         """Вычисление ковариации между X и Y."""
#         # Формула выборочной ковариации: Cov(X,Y) = Sum[(Xi - mean_X) * (Yi - mean_Y)] / (n - 1)
#         if self.n < 2:
#             return 0
#         mean_X = self._mean(self.X)
#         mean_Y = self._mean(self.Y)
#         cov = sum([(x - mean_X) * (y - mean_Y) for x, y in zip(self.X, self.Y)])
#         return cov / (self.n - 1)
#
#     def _std_dev(self, data, mean_val):
#         # Вспомогательный метод для расчета выборочного стандартного отклонения
#         if self.n < 2:
#             return 0
#         variance = sum([(d - mean_val) ** 2 for d in data]) / (self.n - 1)
#         return math.sqrt(variance)
#
#     def pearson_correlation(self):
#         """Вычисление коэффициента корреляции Пирсона между X и Y."""
#         # Формула: r = Cov(X, Y) / (std_dev_X * std_dev_Y)
#         cov = self.covariance()
#         std_X = self._std_dev(self.X, self._mean(self.X))
#         std_Y = self._std_dev(self.Y, self._mean(self.Y))
#
#         if std_X == 0 or std_Y == 0:
#             return 0
#         return cov / (std_X * std_Y)
#
#     def spearman_correlation(self):
#         """Вычисление коэффициента корреляции Спирмена между X и Y."""
#
#         # Расчет на основе разности рангов
#         def get_ranks(data):
#             # Создаем пары (значение, индекс) и сортируем по значению
#             sorted_data = sorted(enumerate(data), key=lambda item: item[1])
#             ranks = {}
#             # Присваиваем ранг
#             for rank, (index, value) in enumerate(sorted_data, 1):
#                 # Упрощенное ранжирование без учета совпадающих рангов (ties)
#                 ranks[index] = rank
#             # Возвращаем ранги в исходном порядке
#             return [ranks[i] for i in range(self.n)]
#
#         ranks_X = get_ranks(self.X)
#         ranks_Y = get_ranks(self.Y)
#
#         # Разность рангов
#         d_squared_sum = sum([(rx - ry) ** 2 for rx, ry in zip(ranks_X, ranks_Y)])
#
#         # Формула Спирмена без учета совпадающих рангов
#         if self.n == 0 or (self.n ** 3 - self.n) == 0:
#             return 0
#         return 1 - (6 * d_squared_sum) / (self.n ** 3 - self.n)
#
#     def plot_scatter(self):
#         """Визуализация данных в виде точечной диаграммы с использованием matplotlib."""
#         plt.figure(figsize=(8, 6))
#         plt.scatter(self.X, self.Y, color='blue', alpha=0.7)
#         plt.title('Точечная диаграмма (X vs Y)')
#         plt.xlabel('Значения X')
#         plt.ylabel('Значения Y')
#         plt.grid(True)
#         plt.show()
# # Пример данных
# X_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Y_data = [5, 18, 25, 35, 42, 55, 68, 80, 88, 95]
#
# # Создаем объект класса
# corr_analysis = Correlation(X_data, Y_data)
#
# # Выводим результаты расчетов
# print(f"Ковариация: {corr_analysis.covariance():.4f}")
# print(f"Коэффициент корреляции Пирсона: {corr_analysis.pearson_correlation():.4f}")
# print(f"Коэффициент корреляции Спирмена: {corr_analysis.spearman_correlation():.4f}")
#
# # Визуализируем данные (раскомментируйте, если запускаете локально)
# # corr_analysis.plot_scatter()
#
# #задание 4
# from scipy import stats
# import pandas as pd
#
#
# class HypothesisTest:
#     """Базовый класс для статистических тестов."""
#
#     def __init__(self):
#         self.p_value = None
#         self.test_result = None
#
#     def run_test(self):
#         """Выполнение соответствующего статистического теста."""
#         raise NotImplementedError("Этот метод должен быть переопределен в дочернем классе.")
#
#     def get_p_value(self):
#         """Получение p-значения из результатов теста."""
#         if self.p_value is None:
#             raise ValueError("Тест еще не был выполнен. Сначала вызовите run_test().")
#         return self.p_value
#
#     def interpret_results(self, alpha=0.05):
#         """Интерпретация результатов на основе заданного уровня значимости (alpha)."""
#         if self.p_value is None:
#             raise ValueError("Тест еще не был выполнен. Сначала вызовите run_test().")
#         print(f"Уровень значимости (alpha): {alpha}, P-значение: {self.p_value:.4f}")
#         if self.p_value < alpha:
#             return "Отвергаем нулевую гипотезу (результат статистически значим)."
#         else:
#             return "Не отвергаем нулевую гипотезу (результат статистически не значим)."
#
#
# class TTest(HypothesisTest):
#     """Класс для выполнения t-теста (одновыборочный, двухвыборочный независимый, двухвыборочный зависимый)."""
#
#     def __init__(self, data1, data2=None, hyp_mean=0):
#         super().__init__()
#         self.data1 = data1
#         self.data2 = data2
#         self.hyp_mean = hyp_mean
#         self.test_type = self._determine_test_type()
#
#     def _determine_test_type(self):
#         if self.data2 is None:
#             return "Одновыборочный t-тест"
#         elif len(self.data1) == len(self.data2):
#             return "Двухвыборочный зависимый t-тест"
#         else:
#             return "Двухвыборочный независимый t-тест"
#
#     def run_test(self):
#         print(f"Выполнение теста: {self.test_type}")
#         if self.test_type == "Одновыборочный t-тест":
#             # stats.ttest_1samp возвращает statistic и pvalue
#             self.test_result = stats.ttest_1samp(self.data1, self.hyp_mean)
#         elif self.test_type == "Двухвыборочный зависимый t-тест":
#             self.test_result = stats.ttest_rel(self.data1, self.data2)
#         elif self.test_type == "Двухвыборочный независимый t-тест":
#             # assumed equal_var=False (Welch's t-test) by default in scipy > 1.8
#             self.test_result = stats.ttest_ind(self.data1, self.data2)
#
#         self.p_value = self.test_result.pvalue
#         return self.test_result
#
#
# class ChiSquareTest(HypothesisTest):
#     """Класс для выполнения критерия хи-квадрат."""
#
#     def __init__(self, contingency_table):
#         super().__init__()
#         # Принимает таблицу сопряженности (список списков или DataFrame)
#         self.table = contingency_table
#
#     def run_test(self):
#         print("Выполнение критерия хи-квадрат (независимости)")
#         # stats.chi2_contingency возвращает statistic, pvalue, dof, expected_freq
#         self.test_result = stats.chi2_contingency(self.table)
#         self.p_value = self.test_result[1]
#         return self.test_result
# # --- Пример 1: Одновыборочный t-тест ---
# data_single = 2
# ttest_1samp = TTest(data_single, hyp_mean=5)
# ttest_1samp.run_test()
# print(ttest_1samp.interpret_results())
#
# print("\n" + "="*40 + "\n")
#
# # --- Пример 2: Двухвыборочный независимый t-тест ---
# data_ind1 = 1
# data_ind2 =2
# ttest_ind = TTest(data_ind1, data2=data_ind2)
# ttest_ind.run_test()
# print(ttest_ind.interpret_results(alpha=0.01))
#
# print("\n" + "="*40 + "\n")
#
# # --- Пример 3: Критерий хи-квадрат ---
# # Таблица сопряженности (например, результаты опроса по полу и предпочтениям)
# contingency_table = 3
# chi2_test = ChiSquareTest(contingency_table)
# chi2_test.run_test()
# print(chi2_test.interpret_results())
#
# #задание 5
# import matplotlib.pyplot as plt
# import numpy as np
# # Импорт необходимых модулей из sklearn
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.pipeline import make_pipeline
# from sklearn.metrics import r2_score, mean_squared_error
# from abc import ABC, abstractmethod
#
#
# class RegressionModel(ABC):
#     """Базовый абстрактный класс для моделей регрессии."""
#
#     def __init__(self):
#         self.model = None
#
#     @abstractmethod
#     def fit(self, X, y):
#         """Обучение модели на данных Х (независимые переменные) и у (зависимая переменная)."""
#         pass
#
#     def predict(self, X):
#         """Предсказание значений y для новых данных X."""
#         if self.model is None:
#             raise ValueError("Модель не обучена. Вызовите fit(X, y) сначала.")
#         # reshape(-1, 1) гарантирует, что X имеет форму (n_samples, n_features)
#         return self.model.predict(X.reshape(-1, 1))
#
#     def evaluate(self, X, y):
#         """Оценка качества модели (R-квадрат, MSE)."""
#         if self.model is None:
#             raise ValueError("Модель не обучена.")
#         predictions = self.predict(X)
#         r2 = r2_score(y, predictions)
#         mse = mean_squared_error(y, predictions)
#         return {"R-квадрат": r2, "MSE": mse}
#
#     def plot_regression(self, X, y):
#         """Визуализация данных и линии регрессии (использовать matplotlib)."""
#         if self.model is None:
#             print("Модель не обучена, невозможно построить график.")
#             return
#
#         plt.figure(figsize=(10, 6))
#         plt.scatter(X, y, color='blue', label='Фактические данные')
#
#         # Создаем диапазон значений для предсказания линии регрессии
#         # X должен быть двумерным массивом для sklearn
#         X_plot = np.linspace(min(X), max(X), 100).reshape(-1, 1)
#         y_plot = self.predict(X_plot)
#
#         plt.plot(X_plot, y_plot, color='red', linewidth=2, label='Линия регрессии')
#         plt.title(f"Регрессионный анализ: {self.__class__.__name__}")
#         plt.xlabel("X (независимая переменная)")
#         plt.ylabel("y (зависимая переменная)")
#         plt.legend()
#         plt.grid(True)
#         # plt.show() # Раскомментируйте, чтобы отобразить график при локальном запуске
#
#
# class LinearRegressionModel(RegressionModel):
#     """Подкласс для выполнения линейной регрессии."""
#
#     def fit(self, X, y):
#         # Используем sklearn.linear_model.LinearRegression
#         self.model = LinearRegression()
#         # reshape(-1, 1) для преобразования одномерного X в двумерный
#         self.model.fit(X.reshape(-1, 1), y)
#
#
# class PolynomialRegressionModel(RegressionModel):
#     """Подкласс для выполнения полиномиальной регрессии (можно задавать степень полинома)."""
#
#     def __init__(self, degree=2):
#         super().__init__()
#         self.degree = degree
#
#     def fit(self, X, y):
#         # Используем конвейер (pipeline) для объединения PolynomialFeatures и LinearRegression
#         self.model = make_pipeline(PolynomialFeatures(degree=self.degree), LinearRegression())
#         # reshape(-1, 1) для преобразования одномерного X в двумерный
#         self.model.fit(X.reshape(-1, 1), y)
# # Создание синтетических данных для примера
# np.random.seed(0)
# # Генерируем данные X в виде одномерного массива
# X_data = np.sort(5 * np.random.rand(80))
# # Генерируем y с небольшим шумом для демонстрации
# y_data = np.sin(X_data) * 10 + np.random.normal(0, 1, X_data.shape)
#
# print("--- Тестирование Линейной модели ---")
# linear_model = LinearRegressionModel()
# linear_model.fit(X_data, y_data)
# metrics_linear = linear_model.evaluate(X_data, y_data)
# print(f"R-квадрат: {metrics_linear['R-квадрат']:.4f}, MSE: {metrics_linear['MSE']:.4f}")
# # linear_model.plot_regression(X_data, y_data)
#
# print("\n--- Тестирование Полиномиальной модели (степень 3) ---")
# poly_model = PolynomialRegressionModel(degree=3)
# poly_model.fit(X_data, y_data)
# metrics_poly = poly_model.evaluate(X_data, y_data)
# print(f"R-квадрат: {metrics_poly['R-квадрат']:.4f}, MSE: {metrics_poly['MSE']:.4f}")
# # poly_model.plot_regression(X_data, y_data)
#
# #задание 6
# import pandas as pd
# import numpy as np
# import random
#
# class Sampling:
#     """Класс, который позволяет осуществлять различные виды выборки из набора данных."""
#
#     def simple_random_sample(self, data, n):
#         """
#         Простая случайная выборка из data размером n.
#         data может быть pandas DataFrame или другим итерируемым объектом.
#         """
#         if isinstance(data, pd.DataFrame):
#             return data.sample(n=n, replace=False)
#         else:
#             # Для списков или других коллекций
#             return random.sample(data, k=n)
#
#     def stratified_sample(self, data: pd.DataFrame, strata: str, n: dict):
#         """
#         Стратифицированная выборка.
#         data - DataFrame, strata - столбец для стратификации,
#         n - словарь, где ключи значения в столбце strata, а значения количество элементов для выборки из каждой страты.
#         """
#         # Группируем по столбцу стратификации и берем sample для каждой группы
#         samples = []
#         for stratum_val, count in n.items():
#             stratum_data = data[data[strata] == stratum_val]
#             # replace=True может потребоваться, если страта меньше нужного n
#             sample = stratum_data.sample(n=count, replace=False)
#             samples.append(sample)
#         return pd.concat(samples)
#
#     def cluster_sample(self, data: pd.DataFrame, cluster_column: str, n_clusters: int):
#         """
#         Кластерная выборка.
#         data - DataFrame, cluster_column - столбец, определяющий кластеры,
#         n_clusters - количество кластеров для выборки.
#         """
#         # Получаем список уникальных кластеров
#         unique_clusters = data[cluster_column].unique()
#         # Случайно выбираем n_clusters из уникальных кластеров
#         selected_clusters = np.random.choice(unique_clusters, size=n_clusters, replace=False)
#         # Фильтруем исходные данные, оставляя только выбранные кластеры
#         return data[data[cluster_column].isin(selected_clusters)]
#
#     def systematic_sample(self, data, k: int):
#         """
#         Систематическая выборка с шагом k.
#         """
#         # Если это DataFrame, работаем с индексами
#         if isinstance(data, pd.DataFrame):
#             indices = np.arange(0, len(data), k)
#             return data.iloc[indices]
#         else:
#             # Для списка
#             return data[::k]
#
# #### **Answer:**
#
# # Пример использования:
# # Создаем демонстрационный DataFrame
# np.random.seed(42)
# data = pd.DataFrame({
#     'ID': range(1, 101),
#     'Score': np.random.randint(50, 100, 100),
#     'Region': np.random.choice(['North', 'South', 'East', 'West'], 100)
# })
#
# sampler = Sampling()
#
# print("--- Простая случайная выборка (n=5) ---")
# simple_sample = sampler.simple_random_sample(data, 5)
# print(simple_sample)
#
# print("\n--- Стратифицированная выборка ---")
# # Выбираем по 2 элемента из каждой страты 'Region'
# strat_sample = sampler.stratified_sample(data, 'Region', {'North': 2, 'South': 2, 'East': 2, 'West': 2})
# print(strat_sample)
#
# print("\n--- Кластерная выборка (n_clusters=2) ---")
# cluster_sample = sampler.cluster_sample(data, 'Region', 2)
# print(cluster_sample['Region'].unique()) # Показывает выбранные кластеры
#
# print("\n--- Систематическая выборка (k=10) ---")
# systematic_sample = sampler.systematic_sample(data, 10)
# print(systematic_sample[['ID', 'Region']])
#
# #задание 7
# class RealString:
#     def __init__(self, basic_string):
#         """Конструктор класса, сохраняет исходную строку."""
#         self.basic_string = basic_string
#         self.length = len(basic_string)
#
#     def __str__(self):
#         """Метод для удобного вывода объекта."""
#         return self.basic_string
#
#     # Реализация методов сравнения, основанных на длине строки (self.length)
#     # Задание требует 3 метода, мы используем один __init__ и, например, __lt__ и __gt__.
#     # Для полного функционала обычно реализуют все 6: __lt__, __le__, __eq__, __ne__, __gt__, __ge__
#
#     def __lt__(self, other):
#         """Метод для оператора '<' (меньше чем)."""
#         if isinstance(other, RealString):
#             return self.length < other.length
#         elif isinstance(other, str):
#             return self.length < len(other)
#         else:
#             raise TypeError(f"Сравнение типа 'RealString' и типа '{type(other).__name__}' не поддерживается.")
#
#     def __gt__(self, other):
#         """Метод для оператора '>' (больше чем)."""
#         if isinstance(other, RealString):
#             return self.length > other.length
#         elif isinstance(other, str):
#             return self.length > len(other)
#         else:
#             raise TypeError(f"Сравнение типа 'RealString' и типа '{type(other).__name__}' не поддерживается.")
#
#     def __eq__(self, other):
#         """Метод для оператора '==' (равно)."""
#         if isinstance(other, RealString):
#             return self.length == other.length
#         elif isinstance(other, str):
#             return self.length == len(other)
#         return NotImplemented  # Позволяет Python попробовать сравнение в другом направлении, если типы разные
# # Создаем объекты класса
# s_apple = RealString("Apple")
# s_яблоко = RealString("Яблоко")
#
# print(f"Строка 1: '{s_apple}' (длина {s_apple.length})")
# print(f"Строка 2: '{s_яблоко}' (длина {s_яблоко.length})")
#
# # Сравнение объектов класса между собой (по количеству символов)
# print(f"\nСравнение объектов (Apple > Яблоко)? {s_apple > s_яблоко}") # False (5 > 6)
# print(f"Сравнение объектов (Apple < Яблоко)? {s_apple < s_яблоко}") # True (5 < 6)
#
# # Сравнение экземпляра класса с обычной строкой
# print(f"\nСравнение с обычной строкой (Яблоко > 'Car')? {s_яблоко > 'Car'}") # True (6 > 3)
# print(f"Сравнение с обычной строкой ('Text' < Apple)? {'Text' < s_apple}") # True (4 < 5)
#
# #задание 8
# import random
#
#
# def run_powerball_simulation(user_numbers, user_powerball, num_simulations=1_000_000):
#     """
#     Моделирует розыгрыши Powerball и считает выигрыши.
#
#     :param user_numbers: Список из 5 выбранных пользователем чисел (1-69).
#     :param user_powerball: Выбранное пользователем число Powerball (1-26).
#     :param num_simulations: Количество моделируемых розыгрышей.
#     """
#     winnings_count = 0
#
#     # Преобразуем числа пользователя в набор (set) для быстрого поиска
#     user_nums_set = set(user_numbers)
#
#     for _ in range(num_simulations):
#         # Выбираем 5 случайных чисел от 1 до 69 (порядок не важен, без повторений)
#         winning_numbers = set(random.sample(range(1, 70), 5))
#
#         # Выбираем 1 случайное число Powerball от 1 до 26
#         winning_powerball = random.randint(1, 26)
#
#         # Проверяем совпадение:
#         # Совпадают ли все 5 основных чисел И совпадает ли число Powerball
#         if winning_numbers == user_nums_set and winning_powerball == user_powerball:
#             winnings_count += 1
#             # В реальной симуляции на миллион розыгрышей это крайне маловероятно
#
#     print(f"\n--- Результаты моделирования {num_simulations:,} розыгрышей ---")
#     print(f"Выигрышных комбинаций найдено: {winnings_count} раз(а)")
#
#     if winnings_count == 0:
#         print("\nКак и ожидалось, вы не выиграли в этой симуляции.")
#     else:
#         print("\nПоздравляем! Вы невероятно удачливы, даже в симуляции!")
#
#
# # --- Пример использования ---
#
# # Выберите свои номера (например, как рекомендовано в тексте)
# my_numbers = [1, 2, 3, 4, 5]
# my_powerball = 6
#
# print(f"Ваши номера: {my_numbers}, Powerball: {my_powerball}")
#
# # Запускаем симуляцию миллион раз
# run_powerball_simulation(my_numbers, my_powerball, num_simulations=1_000_000)
#
# #практика 9
# #задание 1
# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         # pi * r^2
#         return math.pi * self.radius**2
#
#     def perimeter(self):
#         # 2 * pi * r
#         return 2 * math.pi * self.radius
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         # width * height
#         return self.width * self.height
#
#     def perimeter(self):
#         # 2 * (width + height)
#         return 2 * (self.width + self.height)
#
# # --- Тестирование ---
# circle_instance = Circle(5)
# rectangle_instance = Rectangle(4, 6)
#
# print(f"Круг (радиус 5): Площадь = {circle_instance.area():.2f}, Периметр = {circle_instance.perimeter():.2f}")
# print(f"Прямоугольник (4x6): Площадь = {rectangle_instance.area()}, Периметр = {rectangle_instance.perimeter()}")
#
# # Проверка абстрактности:
# try:
#     abstract_shape_instance = Shape()
# except TypeError as e:
#     print(f"\nУспешно вызвана ошибка при попытке создать экземпляр Shape: {e}")
# #задание 2
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     """Абстрактный класс Животное с абстрактными методами."""
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#     @abstractmethod
#     def eat(self):
#         pass
#
# class Dog(Animal):
#     """Класс Собака, наследующийся от Animal."""
#
#     def make_sound(self):
#         print("Woof!")
#
#     def eat(self):
#         print("Dog eating...")
#
# class Cat(Animal):
#     """Класс Кот, наследующийся от Animal."""
#
#     def make_sound(self):
#         print("Meow!")
#
#     def eat(self):
#         print("Cat eating...")
#
# class Bird(Animal):
#     """Класс Птица, наследующийся от Animal."""
#
#     def make_sound(self):
#         print("Chirp!")
#
#     def eat(self):
#         print("Bird eating...")
#
#
#
#
# # Создание экземпляров
# my_dog = Dog()
# my_cat = Cat()
# my_bird = Bird()
#
# print("--- Работаем с собакой ---")
# my_dog.make_sound()
# my_dog.eat()
#
# print("\n--- Работаем с котом ---")
# my_cat.make_sound()
# my_cat.eat()
#
# print("\n--- Работаем с птицей ---")
# my_bird.make_sound()
# my_bird.eat()
#
# #задание 3
# from abc import ABC, abstractmethod
#
#
# class PaymentSystem(ABC):
#     @abstractmethod
#     def process_payment(self, amount):
#         pass
#
#     @abstractmethod
#     def refund_payment(self, payment_id, amount):
#         pass
#
#
# class PayPalPayment(PaymentSystem):
#     def __init__(self, api_key):
#         self.api_key = api_key
#         print(f"PayPal инициализирован с ключом API: {api_key}")
#
#     def process_payment(self, amount):
#         print(f"PayPal: Processing payment of ${amount}")
#
#     def refund_payment(self, payment_id, amount):
#         print(f"PayPal: Refunding payment {payment_id} of ${amount}")
#
#
# class StripePayment(PaymentSystem):
#     def __init__(self, api_key):
#         self.api_key = api_key
#         print(f"Stripe инициализирован с ключом API: {api_key}")
#
#     def process_payment(self, amount):
#         print(f"Stripe: Processing payment of ${amount}")
#
#     def refund_payment(self, payment_id, amount):
#         print(f"Stripe: Refunding payment {payment_id} of ${amount}")
#
#
# # --- Тестирование ---
# paypal_instance = PayPalPayment(api_key="paypal_secret_123")
# stripe_instance = StripePayment(api_key="stripe_live_key_xyz")
#
# print("\n--- Тестирование PayPal ---")
# paypal_instance.process_payment(amount=50.75)
# paypal_instance.refund_payment(payment_id="tx_12345", amount=10.00)
#
# print("\n--- Тестирование Stripe ---")
# stripe_instance.process_payment(amount=120.00)
# stripe_instance.refund_payment(payment_id="ch_abcde", amount=120.00)
#
# #задание 4
# from abc import ABC, abstractmethod
#
# class OrderProcessor(ABC):
#     @abstractmethod
#     def validate_order(self, order):
#         pass
#
#     @abstractmethod
#     def calculate_total(self, order):
#         pass
#
#     @abstractmethod
#     def process_payment(self, order):
#         pass
#
#     @abstractmethod
#     def ship_order(self, order):
#         pass
#
# class StandardOrderProcessor(OrderProcessor):
#     def validate_order(self, order):
#         print(f"Standard: Validating order {order.get('id')}...")
#         if 'items' not in order or not order['items']:
#             return False, "Order has no items."
#         return True, "Order valid."
#
#     def calculate_total(self, order):
#         total = sum(item['price'] * item['quantity'] for item in order['items'])
#         return total
#
#     def process_payment(self, order):
#         print(f"Standard: Оплата заказа {order.get('id')} обрабатывается.")
#
#     def ship_order(self, order):
#         print(f"Standard: Заказ {order.get('id')} отправлен стандартной доставкой.")
#
# class PremiumOrderProcessor(OrderProcessor):
#     def validate_order(self, order):
#         print(f"Premium: Performing extended validation for order {order.get('id')}...")
#         if order.get('customer_type') != 'VIP':
#             print("Premium: Предупреждение: Клиент не VIP.")
#         return True, "Premium order valid."
#
#     def calculate_total(self, order):
#         total = sum(item['price'] * item['quantity'] for item in order['items'])
#         discount = 0.10 if order.get('customer_type') == 'VIP' else 0
#         final_total = total * (1 - discount)
#         return final_total
#
#     def process_payment(self, order):
#         print(f"Premium: Оплата заказа {order.get('id')} обрабатывается через премиум-систему.")
#
#     def ship_order(self, order):
#         print(f"Premium: Заказ {order.get('id')} отправлен быстрой доставкой.")
#
# # --- Тестирование ---
# order1 = {
#     'id': 1,
#     'customer_type': 'Regular',
#     'items': [
#         {'product': 'Laptop', 'price': 1000, 'quantity': 1},
#         {'product': 'Mouse', 'price': 25, 'quantity': 2}
#     ]
# }
#
# order2 = {
#     'id': 2,
#     'customer_type': 'VIP',
#     'items': [
#         {'product': 'Smartphone', 'price': 800, 'quantity': 1}
#     ]
# }
#
# standard_processor = StandardOrderProcessor()
# premium_processor = PremiumOrderProcessor()
#
# def handle_order(processor, order):
#     print(f"\n--- Обработка заказа {order['id']} с помощью {processor.__class__.__name__} ---")
#     is_valid, msg = processor.validate_order(order)
#     if is_valid:
#         total = processor.calculate_total(order)
#         print(f"Итоговая стоимость: ${total:.2f}")
#         processor.process_payment(order)
#         processor.ship_order(order)
#     else:
#         print(f"Ошибка валидации: {msg}")
#
# handle_order(standard_processor, order1)
# handle_order(premium_processor, order1)
# handle_order(standard_processor, order2)
# handle_order(premium_processor, order2)
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



