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
# # задание 4
# class TringleCheker:
#     def __init__(self, a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def is_triangle(self):
#         if not all(isinstance(side, (int, float))for side in [self.a, self.b, self.c,]):
#             return ("нужно вводить только числа")
#
#         if not all (side > 0 for side in [self.a, self.b, self.c]):
#             return "с отрицательными числами ничего не выйдет"
#
#         if (self.a + self.b > self.c) and (self.a +self.c >self.b) and (self.b + self.c > self.a):
#             return "можно построить треугольник"
#         else:
#             return "треугольник построить не возможно"
#
# # задание 5
# class Nikola:
#     def __init__(self, name, age):
#         self.age =age
#         if name == "Николай":
#             self.name =name
#         else:
#             self.name = f"я не {name}, а Николай"
#     def __setattr__(self, name, value):
#         if hasattr(self, name):
#             object.__setattr__(self,name,value)
#         else:
#             raise AttributeError(f"Атрибут '{name}' не может быть добавлен к экземпляру Nikola")
# #задание 6
# class Programmer:
#  RATES = {
#      "Junior":10,
#      "Middle":15,
#      "Senior":20
#  }
#  def __init__(self, name, position):
#      self.name = name
#      self.position = position
#      self.hour = 0
#      self .salary = 0
#      self.senior_rises = 0
#      if self.position in self.RATES:
#          self.rate = self.RATES[self.position]
#      else:
#          self.rate = self.RATES["Junior"]
# def work(self, time):
#     if time>0:
#         self.hours += time
#         self.salary += time * self.rate
# def rise(self):
#     if self.position == "Junior":
#         self.position = "Middle"
#         self.rate = self.RATES["Middle"]
#     elif self.position == "Middle":
#         self.position = "Senior"
#         self.rate = self.RATES["Senior"]
#     elif self.position == "Senior":
#         self.senior_rises += 1
#         self.rate = self.RATES["Senior"] + self.senior_rises
# def into(self):
#     return f"{self.name} {self.hour}ч. {self.salary} тгр."