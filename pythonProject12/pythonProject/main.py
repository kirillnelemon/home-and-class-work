#практика 5
#задание 1
# def shell_sort(data):
#     n=len(data)
#     gap = n // 2
#     while gap > 0:
#         for i in range(gap,n):
#             temp = data [i]
#             j = i
#             while j >= gap and data [j - gap] > temp:
#                 data[j] = data[j - gap]
#                 j -= gap
#             data[j] = temp
#         gap //= 2
#     return  data
#задание 2
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
#         heapify(arr, n, largest)
# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#задание 3
# my_list = [1, 9, 2 ,6 ,24, 56, 15, 11, 22]
# my_list.sort()
# print(my_list)
#Задание 4

def flip(arr, k):
    """
    Вспомогательная функция: меняет порядок первых k элементов списка на обратный.
    Это наша единственная разрешенная операция с лопаткой.
    """
    # top_part - это элементы стопки над лопаткой
    top_part = arr[:k]
    top_part.reverse()
    arr[:k] = top_part

    # Для отладки и понимания процесса
    # print(f"  > Flip (k={k}): {arr}")


def pancake_sort(arr):
    """
    Основная функция пирамидальной сортировки.
    """
    n = len(arr)
    print(f"Начальная стопка: {arr}\n")

    # current_size - это длина неотсортированной части стопки
    for current_size in range(n, 1, -1):
        # 1. Находим индекс максимального элемента в текущем диапазоне
        max_val = max(arr[:current_size])
        max_idx = arr.index(max_val)

        # print(f"--- Ищем максимум {max_val} в диапазоне {current_size} ---")

        # 2. Если максимальный элемент уже на своем месте (внизу текущего диапазона),
        #    просто переходим к следующему шагу.
        if max_idx == current_size - 1:
            continue

        # 3. Поднимаем максимальный элемент наверх (если он еще не там)
        if max_idx != 0:
            # print(f"  Поднимаем {max_val} наверх (k={max_idx + 1})")
            flip(arr, max_idx + 1)

        # 4. Опускаем максимальный элемент на его итоговое место внизу
        # print(f"  Опускаем {max_val} на итоговое место (k={current_size})")
        flip(arr, current_size)

        # print("-" * 30)

    return arr


# --- Пример использования ---

# Задаем стопку оладий различными радиусами
# (например, 6 - самый большой, 1 - самый маленький)
stack =

sorted_stack = pancake_sort(stack)

print("\n--- Финальный результат ---")
print(f"Отсортированная стопка (по убыванию радиуса снизу вверх): {sorted_stack}")
# Ожидаемый результат: 


#практика 6
#задание 1
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

#Практика 7
#задание 1
# class Animal:
#     def __init__(self, nickname):
#
#         self.nickname = nickname
#
#     def __str__(self):
#
#         return f"Это животное  {self.nickname}"
#
#
# class Cat(Animal):
#     def voice(self):
#
#         print(f"{self.nickname} говорит мяу!")
#
#     def run(self):
#
#         print("Побежали!")
#
# class Parrot(Animal):
#     def voice(self):
#
#         print(f"{self.nickname} говорит чик чирик!")
#
#     def fly(self):
#
#         print("Полетели!")
#
# if __name__ == "__main__":
#
#     my_cat = Cat("Котэ")
#     print(my_cat)
#     my_cat.voice()
#     my_cat.run()
#
#     my_parrot = Parrot("птица")
#     print(my_parrot)
#     my_parrot.voice()
#     my_parrot.fly()
#задание 2
