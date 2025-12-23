num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

vibor = input("Выберите операцию: 'сумма' или 'произведение': ")

if vibor == 'сумма':
    result = num1 + num2 + num3
    print(f"Сумма чисел: {result}")
elif vibor == 'произведение':
    result = num1 * num2 * num3
    print(f"Произведение чисел: {result}")
else:
    print("Неверный выбор операции.")



num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

numbers = [num1, num2, num3]

operacia = input(" введите 'макс', 'мин' или 'среднее': ")

if operacia == 'макс':
    result = max(numbers)
    print(f"Максимум из чисел:{result}")
elif operacia == 'мин':
    result = min(numbers)
    print(f"Минимум из чисел: {result}")
elif operacia == 'среднее':
    result = sum(numbers) / len(numbers)
    print(f"Среднее арифметическое чисел: {result}")
else:
    print("Неверный выбор операции.")


#приблизительные значения
mili = 0.000621371
duimi = 39.3701
yardi = 1.09361

meters = float(input("Введите количество метров: "))

wibor = input("Выберите единицу для перевода: введите мили, дюймы или ярды: ")

if wibor == 'мили':
    result = meters * mili
    print(f"{meters} метров в милях: {result} мили")
elif wibor == 'дюймы':
    result = meters * duimi
    print(f"{meters} метров в дюймах:{result} дюймов")
elif wibor == 'ярды':
    result = meters * yardi
    print(f"{meters} метров в ярдах: {result} ярдов")
else:
    print("Неверный выбор единицы измерения.")


