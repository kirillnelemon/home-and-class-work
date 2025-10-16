
import random
left_half = [random.randint(-10, 10) for i in range(10)]
right_half = [random.randint(-10, 10) for i in range(10)]
left_half.sort()
right_half.sort(reverse=True)
print(f"Левая половина (по возрастанию): {left_half}")
print(f"Правая половина (по убыванию): {right_half}")

import random

def merge_lists(list1, list2):
    return list1 + list2
list_a = [1, 2, 3]
list_b = [4, 5, 6]
merged = merge_lists(list_a, list_b)
print(f"Объединенный список: {merged}")
def calculate_power(input_list, power):
    result_list = []
    for num in input_list:
        result_list.append(num ** power)
    return result_list
my_list = [1, 2, 3, 4, 5]
my_power = 2
powered_list = calculate_power(my_list, my_power)
print(powered_list)initial_list = [random.randint(-20, 20) for _ in range(45)]
print("Начальный список:", initial_list)
even_elements = sorted([x for x in initial_list if x % 2 == 0])
odd_elements = sorted([x for x in initial_list if x % 2 != 0])
max_elements = sorted([x for x in initial_list if x == max(initial_list)])
min_elements = sorted([x for x in initial_list if x == min(initial_list)])
alternating_max_min = []
while max_elements or min_elements:
    if max_elements:
        alternating_max_min.append(max_elements.pop(0))
    if min_elements:
        alternating_max_min.append(min_elements.pop(0))
sorted_list = even_elements + alternating_max_min + odd_elements
print("Отсортированный список:", sorted_list)
