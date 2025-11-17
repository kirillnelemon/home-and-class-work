# #задание 1
# import random
#
# spisok = [random.randint(1, 100) for i in range(10)]
# print("Список:", spisok)
# try:
#     chislo = int(input("Введите число для поиска: "))
# except ValueError:
#     print("Ошибка: введено не целое число.")
#     exit()
# try:
#     indeks = spisok.index(chislo)
#     print(f"Число {chislo} найдено. Индекс (позиция от 0): {indeks}")
# except ValueError:
#     # Если метод index() не находит число, он вызывает ошибку ValueError
#     print(f"Число {chislo} не найдено в списке.")
#
# #задание 2
# import random
#
# spisok = sorted([random.randint(1, 100) for i in range(10)])
# print("Список:", spisok)
# try:
#     chislo = int(input("Введите число для поиска: "))
# except ValueError:
#     print("Ошибка ввода.")
#     exit()
# low, high = 0, len(spisok) - 1
# found = False
# while low <= high:
#     mid = (low + high) // 2
#     if spisok[mid] == chislo:
#         found = True
#         break
#     elif spisok[mid] < chislo:
#         low = mid + 1
#     else:
#         high = mid - 1
# if found:
#     print(f"Число {chislo} найдено.")
# else:
#     print(f"Число {chislo} не найдено.")
#     #задание 3
# class Soda:
#     def __init__(self, additive):
#         self.additive =additive
#     def show_my_drink(self):
#         if self.additive:
#             print(f"газировка и {self.additive}")
#         else:
#             print("обычная газировка")
# Soda_with_additive = Soda("Вишня")
# Soda_with_additive.show_my_drink()




