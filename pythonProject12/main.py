def product_of_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
my_list = [1, 2, 3, 4, 5]
print(f"Произведение элементов списка {my_list} равно {product_of_list(my_list)}")
def find_min(numbers):
    if not numbers:
        return None
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value
my_list = [10, 5, 20, 3, 15]
result = find_min(my_list)
print(f"Минимальное значение в списке: {result}")
import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def count_prime_numbers(numbers):
    prime_count = 0
    for number in numbers:
        if is_prime(number):
            prime_count += 1
    return prime_count
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]
result = count_prime_numbers(my_list)
print(f"Количество простых чисел в списке: {result}")
def remove_and_count(numbers, number_to_remove):
    count = 0
    while number_to_remove in numbers:
        numbers.remove(number_to_remove)
        count += 1
    return count
my_list = [1, 5, 3, 5, 2, 5, 4]
number_to_remove = 5
removed_count = remove_and_count(my_list, number_to_remove)
print(f"Количество удаленных элементов: {removed_count}")
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
