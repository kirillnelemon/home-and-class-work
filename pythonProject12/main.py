import random

def linear_search(arr, target):
    """Performs linear search for a target value in a list."""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 1. Initialize four lists of integers (example data)
list1 = [random.randint(1, 50) for i in range(10)]
list2 = [random.randint(1, 50) for i in range(10)]
list3 = [random.randint(1, 50) for i in range(10)]
list4 = [random.randint(1, 50) for i in range(10)]

print(f"Список 1: {list1}")
print(f"Список 2: {list2}")
print(f"Список 3: {list3}")
print(f"Список 4: {list4}")

# 2. Combine them into a fifth list
fifth_list = list1 + list2 + list3 + list4
print(f"\nОбъединенный список: {fifth_list}")

# 3. Get user choice for sorting order
sort_order_choice = input("\nВыберите порядок сортировки (1 - возрастание, 2 - убывание): ")

if sort_order_choice == '1':
    fifth_list.sort()
    print(f"Отсортированный по возрастанию список: {fifth_list}")
elif sort_order_choice == '2':
    fifth_list.sort(reverse=True)
    print(f"Отсортированный по убыванию список: {fifth_list}")
else:
    print("Неверный выбор сортировки. Список оставлен без сортировки.")

# 4. Find user-entered value using linear search
user_value_to_find = int(input("Введите целое число для поиска: "))
index = linear_search(fifth_list, user_value_to_find)

if index != -1:
    print(f"Значение {user_value_to_find} найдено в списке по индексу: {index}.")
else:
    print(f"Значение {user_value_to_find} не найдено в списке.")


    def binary_search(arr, target):
        """Реализация бинарного поиска (итеративный метод)."""
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2  # Вычисление среднего индекса
            if arr[mid] == target:
                return mid  # Элемент найден
            elif arr[mid] < target:
                left = mid + 1  # Сужаем область поиска до правой половины
            else:
                right = mid - 1  # Сужаем область поиска до левой половины
        return -1  # Элемент не найден


    # Исходные списки (с возможными дубликатами для примера)
    listA = [1, 2, 3, 4, 5, 1]
    listB = [4, 5, 6, 7, 8, 4]
    listC = [7, 8, 9, 10, 11, 7]
    listD = [10, 11, 12, 13, 14, 10]

    # Объединение списков
    combined_list = listA + listB + listC + listD

    # Получение уникальных элементов с использованием set()
    unique_elements_set = set(combined_list)
    unique_elements_list = list(unique_elements_set)

    print(f"Список уникальных элементов (несортированный): {unique_elements_list}")

    # Выбор пользователя для сортировки
    sort_order_input_2 = input("Выберите порядок сортировки (asc/desc): ")
    if sort_order_input_2.lower() == 'desc':
        unique_elements_list.sort(reverse=True)
        print(f"Список отсортирован по убыванию: {unique_elements_list}")
    else:
        unique_elements_list.sort()
        print(f"Список отсортирован по возрастанию: {unique_elements_list}")

    # Поиск значения, введенного пользователем
    user_value_input_2 = input("Введите целое число для поиска: ")
    try:
        user_value_2 = int(user_value_input_2)
        index_2 = binary_search(unique_elements_list, user_value_2)

        if index_2 != -1:
            print(f"Значение {user_value_2} найдено в списке уникальных элементов по индексу: {index_2}")
        else:
            print(f"Значение {user_value_2} не найдено в списке.")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")