# Задание 1: FizzBuzz
print("=== Задание 1 ===")
number = int(input("Введите число от 1 до 100: "))

if number < 1 or number > 100:
    print("Ошибка! Число должно быть от 1 до 100")
else:
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Задание 2: Возведение в степень
print("\n=== Задание 2 ===")
num = float(input("Введите число: "))
print("Выберите степень (от 0 до 7):")

for i in range(8):
    print(f"{i} - {i}-я степень")

choice = int(input("Ваш выбор: "))

if choice < 0 or choice > 7:
    print("Ошибка! Степень должна быть от 0 до 7")
else:
    result = 1
    for i in range(choice):
        result = result * num
    print(f"{num} в степени {choice} = {result}")

# Задание 3: Стоимость разговора
print("\n=== Задание 3 ===")
cost = float(input("Введите стоимость разговора: "))

print("Выберите оператора:")
print("1 - МТС")
print("2 - Билайн")
print("3 - Мегафон")
print("4 - Теле2")

from_operator = int(input("С какого оператора звоните (1-4): "))
to_operator = int(input("На какой оператор звоните (1-4): "))

if from_operator == to_operator:
    final_cost = cost * 0.8  # скидка 20%
elif (from_operator == 1 and to_operator == 2) or (from_operator == 2 and to_operator == 1):
    # МТС \\ Билайн
    final_cost = cost * 1.2  # наценка 20%
elif (from_operator == 3 and to_operator == 4) or (from_operator == 4 and to_operator == 3):
    # Мегафон \\ Теле2
    final_cost = cost * 1.1  # наценка 10%
else:
    # остальные
    final_cost = cost * 1.5  # наценка 50%

print(f"Итоговая стоимость разговора: {final_cost:.2f} руб.")

# Задание 4: Зарплата менеджеров
print("\n=== Задание 4 ===")

managers = 3
salaries = []
sales_list = []

for i in range(managers):
    sales = float(input(f"Введите уровень продаж для менеджера {i + 1}: "))
    sales_list.append(sales)

    base_salary = 200

    if sales < 500:
        bonus = sales * 0.03
    elif sales >= 500 and sales <= 1000:
        bonus = sales * 0.05
    else:
        bonus = sales * 0.08

    total_salary = base_salary + bonus
    salaries.append(total_salary)
    print(f"Зарплата менеджера {i + 1}: {total_salary:.2f}$")

best_index = 0
best_sales = sales_list[0]

for i in range(1, managers):
    if sales_list[i] > best_sales:
        best_sales = sales_list[i]
        best_index = i

salaries[best_index] += 200
print(f"\nЛучший менеджер: №{best_index + 1} с продажами {best_sales:.2f}$")
print("Ему начислена премия 200$")

print("\nИтоговые зарплаты:")
for i in range(managers):
    print(f"Менеджер {i + 1}: {salaries[i]:.2f}$")