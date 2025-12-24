
'''
-----------------------------------------ПРАКТИКА 1------------------------------------------------------------
'''
#1)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
choice = input("выберите 'сумма' или 'произвдение': ")
if choice == 'сумма':
 print("СУММА:" , a + b + c)
elif choice == 'произведение':
 print("ПРОИЗВЕДЕНИЕ:" , a * b * c)
else:
    print("ошибка, выберите сумму или произведение:")
#2)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
choice = input("выберите 'максимум' или 'минимум' или 'среднее арифметическое': ")
if choice == 'максимум':
 print("максимум:", max(a, b, c))
elif choice == 'минимум':
     print("минимум:" , min(a, b, c))
elif choice == 'среднее арифметическое':
   print("СРЕДНЕЕ АРИФМЕТИЧЕСКОЕ:" , (a + b + c) /3)
else:
    print("ошибка, выберите минимум или максимум или среднее арифмитическое:")
#3)
meters = float(input("Введите количество метров: "))
choice = input("Выберите 'ярды', 'дюймы' или 'мили': ")
if choice == 'мили':
    print("Получилось:", round(meters * 0.000621371, 2))
elif choice == 'дюймы':
    print("Получилось:", round(meters * 39.3701, 2))
elif choice == 'ярды':
    print("Получилось:", round(meters * 1.09361, 2))
else:
    print("Ошибка, выберите: 'ярды', 'мили' или 'дюймы'")
# '''
# -----------------------------------------ПРАКТИКА 2------------------------------------------------------------
# '''
#1)
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
summ = a + b + c
product = a * b * c
print("Сумма чисел:", summ)
print("Произведение чисел:", product)
#2)
gross = float(input("введите зп:"))
credit = float(input("введите платеж за кредит:"))
home = float(input("введите долг за коммуналку:"))
summ = gross - credit - home
print("осталось:", summ)
#3)
d1 = int(input("введите длину 1 диагонали:"))
d2 = int(input("введите длину 2 диагонали:"))
area = (d1*d2)/2
print("площадь ромба:", area)
# 4)
print("To be", "or not" , "to be" , sep ='\n' , end= ' ')
#5)
print("'Life is what happens\n  when\n    you're busy making other plans'\n      John Lennon.")
# '''
# -----------------------------------------ПРАКТИКА 3------------------------------------------------------------
# '''
#1)
print("=" * 30)
try:
    number = int(input("введите число от 1 до 100: "))
    if 1 <= number <= 100:
        if number % 3 == 0 and number % 5 == 0:
            print("Fizz Buzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)
    else:
       print("ошибка: число должно быть в диапазоне от 1 до 100")

       #print()
#2)
x = int(input("введите число:"))
for i in range(8):
    print(x,"^" , i ,  "=" , x**i)
#3)
cost = float(input("введите стоимость разговора:"))
print("выберите оператора, с которого звонят:")
print("1 - МТС\n2 - Мегафон\n3 - Билайн")
from_op = int(input("введите номер:"))
if from_op == 1:
    from_name = ("МТС")
elif from_op == 2:
    from_name = ("Мегафон")
elif from_op == 3:
    from_name = ("Билайн")
else:
    print("ошибка: нет такого оператора!")
    exit()
print("выберите оператора , на который звонят:")
print("1 - МТС\n2 - Мегафон\n3 - Билайн")
to_op = int(input("введите номер:"))
if to_op == 1:
    to_name = ("МТС")
elif to_op == 2:
    to_name = ("Мегафон")
elif to_op == 3:
    to_name = ("Билайн")
else:
    print("ошибка:нет такого оператора!")
    exit()
print("звонок с" , from_name , "на" , to_name)
print("стоимость разговора:" , cost, "руб.")
#4)
base = 200
sales = []
for i in range(3):
    s = int(input("продажи менеджера" + str(i+1 ) + ": "))
    sales.append(s)
salaries = []
if s <= 500:
    percent = 0.03
elif s <= 1000:
   percent = 0.05
else:
    percent = 0.08
salary = base + s * percent
salaries.append(salary)
best = max(sales)
best_index = sales.index(best)
salaries[best_index] += 200
for i in range(3):
    print("менеджер" , i+1 , "зарплата = ", salaries[i])
    print("лучший менеджер:" , best_index+1)
# '''
# -----------------------------------------ПРАКТИКА 4------------------------------------------------------------
# '''
#1)
start = int(input("введите начало диапазона: "))
end = int(input("введите конец диапазона: "))
if start > end:
    start, end = end, start
for num in range(start, end+1):
    if num % 7 == 0:
        print(num)
#2)
a = int(input("введите первое число:"))
b = int(input("введите второе число:"))
start = min(a, b)
end = max(a, b)
print("\n1. Все числа диапазона:")
for i in range(start, end + 1):
    print(i, end=" ")
print("\n\n2. Все числа в убывающем порядке:")
for i in range(end, start - 1, -1):
    print(i, end=" ")
print("\n\n3. Числа, кратные 7:")
for i in range(start, end + 1):
    if i % 7 == 0:
        print(i, end=" ")
print("\n\n4. Количество чисел, кратных 5:")
count = 0
for i in range(start, end + 1):
    if i % 5 == 0:
        count += 1
print(count)
#3)
start = int(input("введите начало диапазона: "))
end = int(input("введите конец диапазона: "))
start, end = sorted((start, end))
for number in range(start, end + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
# '''
# -----------------------------------------ПРАКТИКА 5------------------------------------------------------------
# '''
#1)
number = int(input("введите число для умножения:"))
print(f"\n таблица умножения для числа {number}")
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
#2)
print("\nКонвертер валют")
print("1. Рубли -> Доллары")
print("2. Доллары -> Рубли")
choice = int(input("Выберите вариант (1 или 2): "))
if choice == 1:
    rub = float(input("Введите сумму в рублях: "))
    usd = rub / 100  # курс условный: 1$ = 100 руб
    print(f"{rub} руб. = {usd:.2f} $")
elif choice == 2:
    usd = float(input("Введите сумму в долларах: "))
    rub = usd * 100
    print(f"{usd} $ = {rub:.2f} руб.")
else:
    print("Неверный выбор")
#3)
start = int(input("\nВведите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
if start > end:
    start, end = end, start
while True:
    num = int(input("Введите число из диапазона: "))
    if start <= num <= end:
        break
    else:
        print("Число вне диапазона. Попробуйте снова.")
for i in range(start, end + 1):
    if i == num:
        print(f"!{i}!", end=" ")
    else:
        print(i, end=" ")
print()
#4)
import random
import time
secret = random.randint(1, 500)
attempts = 0
print("\nЯ загадал число от 1 до 500. Попробуй угадать (0 - выход).")
start_time = time.time()
while True:
    guess = int(input("Ваш вариант: "))
    if guess == 0:
        print("Вы сдались. Игра окончена.")
        break
    attempts += 1
    if guess < secret:
        print("Моё число больше.")
    elif guess > secret:
        print("Моё число меньше.")
    else:
        end_time = time.time()
        print(f"Поздравляю! Вы угадали число {secret}")
        print(f"Количество попыток: {attempts}")
        print(f"Время игры: {round(end_time - start_time, 2)} секунд")
        break
# '''
# -----------------------------------------ПРАКТИКА 6------------------------------------------------------------
# '''
#1)
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
lst1 = [2, 3, 4]
print("Задание 1:", multiply_list(lst1))
#2)
def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum
lst2 = [5, 2, 9, -3, 7]
print("Задание 2:", find_min(lst2))
#3)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def count_primes(numbers):
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count
lst3 = [2, 3, 4, 5, 10, 11]
print("Задание 3:", count_primes(lst3))
#4)
def remove_number(numbers, value):
    count = numbers.count(value)
    new_list = []
    for num in numbers:
        if num != value:
            new_list.append(num)
    print("Задание 4: количество удалённых элементов:", count)
    return new_list
lst4 = [1, 2, 3, 2, 4, 2]
lst4 = remove_number(lst4, 2)
print("Задание 4: новый список:", lst4)
#5)
def merge_lists(list1, list2):
    return list1 + list2
a = [1, 2, 3]
b = [4, 5, 6]
print("Задание 5:", merge_lists(a, b))
#6)
# Возведение элементов списка в степень
def power_list(numbers, power):
    result = []
    for num in numbers:
        result.append(num ** power)
    return result
lst6 = [1, 2, 3, 4]
print("Задание 6:", power_list(lst6, 3))
# '''
# -----------------------------------------ПРАКТИКА 7------------------------------------------------------------
# '''
#1)
from random import randint
n = 10
mylist = []
for i in range (n):
   mylist.append(randint(1,99))
print(f"неотсортированный список: {mylist}")
i = 0 # первая ячейка
while i < n - 1: # пока i меньше последнего элемента
    m = i # индекс ячейки с минимальным значением
    j = i + 1 # поиск осуществляем со следующей ячейки
    while j < n:
        if mylist [j] < mylist [m]:
            m = j # сохраняем в m номер найденного минимума
        j += 1
    mylist[i] , mylist[m] =  mylist[m] , mylist[i]
    i += 1
print(f"отсортированный список: {mylist}")
#2)
mylist = ["apple" , "banana" , "cherry" , "date" , "apricot"]
print(f"неотсортированный список: {mylist}")
from random import randint
#3)
N = 15
mylist = [randint(1, 100) for _ in range(N)]
print(f"Неотсортированный список: {mylist}")
iterations = 0
for i in range(1, N):
    key = mylist[i]
    j = i - 1
    while j >= 0 and mylist[j] < key:
        mylist[j + 1] = mylist[j]
        j -= 1
        iterations += 1
    mylist[j + 1] = key
    iterations += 1
print(f"Отсортированный список (по убыванию): {mylist}")
print(f"Количество итераций: {iterations}")
print("--"*50)
#4)
words = ["apple", "banana", "cherry", "date", "apricot"]
print("Исходный список:", words)
n = len(words)
j = 0
for i in range(1, n):
    key = words[i]#apple
    j = i - 1#1-1 0
    # Сдвигаем элементы вправо, пока они больше key
    while j >= 0 and words[j] > key:
        words[j + 1] = words[j]
        j -= 1
    words[j + 1] = key
print("Отсортированный список:", words)
print("--"*50)
#5)
arr = [10, 3, 8, 1, 7, 5, 9, 2, 6, 4]
k = 3
print("Исходный массив:", arr)
fixed_value = arr[k]
print(f"Фиксируем элемент на индексе {k}: {fixed_value}")
other_elements = []
for i in range(len(arr)):
    if i != k:
        other_elements.append(arr[i])
n = len(other_elements)
for i in range(n):
    for j in range(0, n - i - 1):
        if other_elements[j] > other_elements[j + 1]:
            other_elements[j], other_elements[j + 1] = other_elements[j + 1], other_elements[j]
left_part = other_elements[:k]
right_part = other_elements[k:]
result = left_part + [fixed_value] + right_part
print("Результат:", result)
# '''
# -----------------------------------------ПРАКТИКА 8------------------------------------------------------------
# '''
#1)
points_to_letters = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'С', 'Т'],
    2: ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'],
    3: ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
    4: ['F', 'H', 'V', 'W', 'Y', 'Й', 'Р', 'Ы'],
    5: ['K', 'Ж', 'З', 'Ч', 'Ц'],
    8: ['J', 'X', 'Ш', 'Э', 'Ю', 'Х'],
    10: ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
}
dictionnary = points_to_letters
gamers = {}  # словарь игрока
count_user = int(input("сколько человек будет играть?:"))
for i in range(count_user):
    name = input("введите имя игрока:").strip()
    if not name:
        name = f"Игрок_{i+1}"
    gamers[name] = 0
print(f"список игроков: \n{gamers}")
# 10 раундов
for raund in range(10):
    for gamer in gamers.keys():
        print("*"*11)
        print(f"ходит игрок {gamer}")
        answer = input("введите слово:").strip().upper()
        for i in answer:
            for key, value in dictionnary.items():
                if i in value:
                    gamers[gamer] += key
                    break  # чтобы не начислять очки дважды
print("игра окончена! \n таблица игроков:")
for key, value in gamers.items():
    print(f"{key} -> {value} баллов")
result_user = ''
result_value = -1
for key, value in gamers.items():
    if result_value < value:
        result_value = value
        result_user = key
print(f"победитель: {result_user}")
#2)
backpack = {'зажигалка':20, 'компас':100, 'фрукты':500, 'рубашка':300,
            'термос':1000, 'аптечка':200, 'куртка':600, 'бинокль':400,
            'удочка':1300, 'салфетки':40, 'бутерброды':800, 'палатка':5500,
            'спальный мешок':2500, 'изолента':250, 'котел':3000
}
max_mass = int(input("введите максимальный вес для похода: "))
curr_mass = 0  # одна переменная
while curr_mass < max_mass:
    print(backpack)
    answer = input("что вы хотите взять с собой: ").strip().lower()
    if answer in backpack:              # проверяем, что предмет существует
        curr_mass += backpack[answer]   # добавляем вес
    else:
        print("такого предмета нет")
print(f"рюкзак заполнен, текущая масса: {curr_mass}")
#3)
contacts = {
    "Иван": {
        "телефон": "+48 600 000 001",
        "ютюб": "https://youtube.com/@ivan",
        "вк": "https://vk.com/ivan",
        "телеграм": "https://t.me/ivan"
    },
    "Мария": {
        "телефон": "+48 600 000 002",
        "ютюб": "https://youtube.com/@maria",
        "вк": "https://vk.com/maria",
        "телеграм": "https://t.me/maria"
    }
}
name = input("Введите имя контакта: ")
if name in contacts:
    info = contacts[name]
    print("Телефон:", info["телефон"])
    print("YouTube:", info["ютюб"])
    print("VK:", info["вк"])
    print("Telegram:", info["телеграм"])
else:
    print("Контакт не найден.")
# '''
# -----------------------------------------ПРАКТИКА 9------------------------------------------------------------
# '''
#эксперимент монте-карло
import datetime
from random import randint
def getbirthday(numberOfBirthdays):
    birthdays = [] # список дней рождений
    for i in range(numberOfBirthdays):
        # год в нашей имитации роли не играет,
        # лишь бы в объектах дней рождения он был одинаков
        start0Year = datetime.date(2000, 1, 1)
        # случайный день года
        randomNumberOfDays = datetime.timedelta(randint(0, 364))
        birthday = start0Year + randomNumberOfDays
        birthdays.append(birthday) # добавляем в список
    return birthdays
'''
принимает список дней рождений. обрабатывает его и возвращает совпадения в
датах, которые встречаются несколько раз
'''
def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None # даты не совпадают, выходим из программы
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA # даты совпали
# MAIN
def main():
    # кортеж месяцев в году
    Months = ('Jan' , 'Feb' , 'Mar' , 'Apr' , 'May' , "Jun" ,
              "Jul" , "Aug" , "Sep" , "Oct" , "Nov" , "Dec")
    print("Добро пожаловать в приложение для симуляции совпадения "
          "дат рождения")
    while True: # апрашвает данные, пока пользователь
        # не введет допустимые значения
        print("сколько симуляций вы хотите сделать \n P.S. max = 100")
        response = input("--->")
        if response.isdecimal() and 0 < int(response) <= 100:
            numBDdays = int(response)
            break
    print()
    # генерируем и отображаем дни рождения
    birthdays = getbirthday(numBDdays)
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(", ", end="")
        months = Months[birthday.month - 1]
        dateText = "{} {}".format(months, birthday.day)
        print(dateText, end="")
    print()
    print()
    print(f"генерация {numBDdays} случайных симуляций")
    input("для продолжения введите Enter...")
    print("запуск 100000 симуляций")
    simMatch = 0
    for i in range(100000):
        if i % 10000 == 0 and i != 0:
            print(i, "запущена симуляция...")
        birthdays = getbirthday(numBDdays)
        if getMatch(birthdays) != None:
            simMatch += 1
    print("было выполнено 100000 симуляций.")
    probability = round(simMatch / 100000 * 100, 2)
    print("процент попадения", probability, "%")
    print("количество дат для исследования:", numBDdays)
    print("количество циклов симуляции:", simMatch)
if __name__ == '__main__':
    main()
#1 вопрос
# др пооказаны как объекты datetime.date где фиксируется год
# а меняются только месяц и день
# 2вопрос
# надо изменить или в крайнем случае удалить часть условия
# f response.isdecimal() and 0 < int(response) <= 100:
# на
# if response.isdecimal() and int(response) > 0:
# теперь можно ввести любое количество
#
# 3 вопрос
# прога выдаст ошибку тк переменная используется хотя ее нет
# NameError: name 'numBDdays' is not defined
# 4 вопрос
# Months = ('January', 'February', 'March', 'April', 'May', 'June',
#           'July', 'August', 'September', 'October', 'November', 'December')
# 5 вопрос
# было if i % 100 == 0:
# стало if i % 1000 == 0:
# '''
# --------------------------ПРАКТИКА 10------------------------------------------------------------
# '''
#1)
print('"Don`t compare yourself with anyone in this world...if you do so, you are insulting\n'
      'yourself."\n'
      '\n'
      'Bill Gates')
#2)
def get_even_numbers(num1, num2):
    start = min(num1, num2)
    end = max(num1, num2)
    even_numbers = []
    for number in range(start, end + 1):
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
result = get_even_numbers(3, 12)
print(f"четные числа: {result}")
#3)
def xz(side_length, symbol, is_filled):
    for row in range(side_length):
        line = ""
        for col in range(side_length):
            if is_filled:
                line += symbol + " "
            else:
                if row == 0 or row == side_length - 1 or col == 0 or col == side_length - 1:
                    line += symbol + " "
                else:
                    line += "  "
        print(line)
print("заполненный квадрат 6x6:")
xz(6, '#', True)
print("\nпустой квадрат 6x6:")
xz(6, '#', False)
# '''
# --------------------------ПРАКТИКА 11------------------------------------------------------------
'''
import random
class Number:
    def __init__(self):
        # сформировать список случайных чисел
        self.grades = [random.randint(-5, 12) for _ in range(10)]
    def show_grades(self):
        print("Список оценок:", self.grades)
    def sort_grades(self):
        avg = sum(self.grades) / len(self.grades)
        if avg > 0:
            # сортируем первые три элемента списка по возрастанию
            self.grades[:3] = sorted(self.grades[:3])
        else:
            # сортируем только первый элемент
            self.grades[0] = sorted(self.grades[:1])

        # остальные элементы в обратном порядке
        self.grades[3:] = sorted(self.grades[3:], reverse=True)
        print("отсортированный список оценок:", self.grades)
# пример использования
number = Number()
number.show_grades()  # показываем исходный список оценок
number.sort_grades()  # сортируем и показываем отсортированный список
2)
class Number:
    def __init__(self, grades):
        self.grades = grades
    def show_grades(self):
        print("cписок оценок:", self.grades)
    def retake_exam(self, index, new_grade):
        self.grades[index] = new_grade
    def check_scholarship(self):
        avg = sum(self.grades) / len(self.grades)
        if avg >= 10.7:
            print("ура, стипендия.")
        else:
            print("лох, без стипендии остался.")
    def sort_grades(self):
        avg = sum(self.grades) / len(self.grades)
        if avg > 0:
            self.grades[:3] = sorted(self.grades[:3])
        else:
            self.grades[0] = sorted(self.grades[:1])
        self.grades[3:] = sorted(self.grades[3:], reverse=True)
        print("отсортированный список:", self.grades)
# Пример данных
grades = [8, 9, 6, 7, 11, 5, 12]
number = Number(grades)
while True:
    print("\n1. показать оценки")
    print("2. пересдать экзамен")
    print("3. проверить стипендию")
    print("4. выйти и отсортировать оценки")
    choice = input("выберите действие: ")
    if choice == '1':
        number.show_grades()
    elif choice == '2':
        index = int(input("введите номер экзамена: "))
        new_grade = int(input("введите новую оценку: "))
        number.retake_exam(index, new_grade)
    elif choice == '3':
        number.check_scholarship()
    elif choice == '4':
        number.sort_grades()
        break
    else:
        print("неверный выбор!")
# ====================== 3 задание ==================
# def bubble_sort(arr):
#     for i in range(len(arr)):
#         swapped = False
#         for j in range(len(arr) - 1 - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         if not swapped:
#             break
#     return arr
# # пример
# arr = [64, 34, 25, 12, 22, 11, 90]
# print(bubble_sort(arr))
# '''
# --------------------------ПРАКТИКА 12------------------------------------------------------------
# '''
#1)
ids = [103, 15, 17, 24]
phones = [79028029311, 79124956827, 79223000257, 79197058606]
while True:
    print("\nменю:")
    print("1. отсортировать по идентификационным кодам")
    print("2. отсортировать по номерам телефона")
    print("3. показать список пользователей")
    print("4. выход")
    choice = input("выберите пункт: ")
    if choice == "1":
        # сортировка по ids
        for i in range(len(ids) - 1):
            for j in range(i + 1, len(ids)):
                if ids[i] > ids[j]:
                    ids[i], ids[j] = ids[j], ids[i]
                    phones[i], phones[j] = phones[j], phones[i]
        print("список отсортирован по ID.")
    elif choice == "2":
        # сортировка по телефону
        for i in range(len(phones) - 1):
            for j in range(i + 1, len(phones)):
                if phones[i] > phones[j]:
                    phones[i], phones[j] = phones[j], phones[i]
                    ids[i], ids[j] = ids[j], ids[i]
        print("список отсортирован по телефонам")
    elif choice == "3":
        print("\nпользователи:")
        for i in range(len(ids)):
            print(ids[i], phones[i])
    elif choice == "4":
        print("выход")
        break
    else:
        print("неверный выбор")
#2)
Списки: названия книг и годы выпуска
titles = ["872 дня блокадного Ленинграда", "9 негритят", "Кладбище домашних животных", "Гарри Поттер и Тайная комната"]
years = [2000, 2022, 1977, 1967]
while True:
    print("\nменю:")
    print("1. отсортировать по названиям книг")
    print("2. отсортировать по годам выпуска")
    print("3. вывести список книг")
    print("4. выход")
    choice = input("выберите пункт: ")
    if choice == "1":
        # сортировка по названиям
        for i in range(len(titles) - 1):
            for j in range(i + 1, len(titles)):
                if titles[i] > titles[j]:
                    titles[i], titles[j] = titles[j], titles[i]
                    years[i], years[j] = years[j], years[i]
        print("Отсортировано по названиям книг.")
    elif choice == "2":
        # сортировка по годам выпуска
        for i in range(len(years) - 1):
            for j in range(i + 1, len(years)):
                if years[i] > years[j]:
                    years[i], years[j] = years[j], years[i]
                    titles[i], titles[j] = titles[j], titles[i]
        print("отсортировано по годам выпуска")
    elif choice == "3":
        print("\nсписок книг:")
        for i in range(len(titles)):
            print(titles[i], "-", years[i])
    elif choice == "4":
        print("выход из программы")
        break
    else:
        print("неверный пункт меню")
# '''
# --------------------------ПРАКТИКА 13------------------------------------------------------------
# '''
#1)
def linear_search(arr, target):
     for i, value in enumerate(arr):
        if value == target:
            return i
    return -1
def main_task1():
    list1 = [5, 2, 8, 1, 9]
    list2 = [4, 7, 2, 6, 4]
    list3 = [10, 15, 12, 11]
    list4 = [22, 18, 16, 14, 13]
    print("список 1:", list1)
    print("список 2:", list2)
    print("список 3:", list3)
    print("список 4:", list4)
    combined_list = list1 + list2 + list3 + list4
    print("\nобъединенный список:", combined_list)
    while True:
        order = input("\nвыберите сортировку 1) по возрастанию, 2) по убыванию: ")
        if order in ['1', '2']:
            break
        print("выберете 1 или 2")
    if order == '1':
        combined_list.sort()
        print("отсортировано по возрастанию:", combined_list)
    else:
        combined_list.sort(reverse=True)
        print("отсортировано по убыванию:", combined_list)
    try:
        search_value = int(input("\nвведите значение для поиска: "))
        index = linear_search(combined_list, search_value)
        if index != -1:
            print(f"значение {search_value} найдено на позиции {index + 1}")
        else:
            print(f"значение {search_value} не найдено в списке")
    except ValueError:
        print("ошибка")
main_task1()
#2)
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1
list1 = [11, 22, 33]
list2 = [44, 55, 66]
list3 = [77, 88, 99]
list4 = [100, 111, 122]
combined_list = list1 + list2 + list3 + list4
print(f"Объединенный список: {combined_list}")
sort_choice = input("Выберите тип сортировки (asc/desc): ")
if sort_choice.lower() == 'desc':
    combined_list.sort(reverse=True)
    print(f"Список отсортирован по убыванию: {combined_list}")
else:
    combined_list.sort()
    print(f"Список отсортирован по возрастанию: {combined_list}")
try:
    user_value = int(input("Введите значение для поиска: "))
    index = linear_search(combined_list, user_value)
    if index != -1:
        print(f"Значение {user_value} найдено в списке на позиции {index}.")
    else:
        print(f"Значение {user_value} не найдено в списке.")
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите целое")
2)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
def get_unique_elements(*lists):
    all_elements = []
    for lst in lists:
        all_elements.extend(lst)
    unique_elements = []
    for element in all_elements:
        if all_elements.count(element) == 1:
            unique_elements.append(element)
    return unique_elements
def main_task2():
    list1 = [5, 2, 8, 1, 9, 100]
    list2 = [3, 7, 2, 6, 4, 100]
    list3 = [10, 15, 12, 11, 200]
    list4 = [20, 18, 16, 14, 13, 300]
    print("список 1:", list1)
    print("список 2:", list2)
    print("список 3:", list3)
    print("список 4:", list4)
    unique_list = get_unique_elements(list1, list2, list3, list4)
    print("\nуникальные элементы:", unique_list)
    if not unique_list:
        print("нет уникальных элементов!")
        return
    while True:
        order = input("\nвыберите сортировку 1) по возрастанию, 2) по убыванию: ")
        if order in ['1', '2']:
            break
        print("введите 1 или 2")
    if order == '1':
        unique_list.sort()
        print("отсортировано по возрастанию:", unique_list)
    else:
        unique_list.sort(reverse=True)
        print("отсортировано по убыванию:", unique_list)
    try:
        search_value = int(input("\nвведите значение для поиска: "))
        search_list = unique_list.copy()
        if order == '2':
            search_list.sort()
        index = binary_search(search_list, search_value)
        if index != -1:
            if order == '1':
                actual_index = index
            else:
                actual_index = len(unique_list) - 1 - index
            print(f"значение {search_value} найдено на позиции {actual_index + 1}")
            print(f"cписок: {unique_list}")
        else:
            print(f"значение {search_value} не найдено в списке")
    except ValueError:
        print("ошибка, введите целое число")
main_task2()
# '''
# --------------------------ПРАКТИКА 14------------------------------------------------------------
# '''
import random
import sys
HEARTS = chr(9827)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'
'''
black jack - классическая карточ игра
известная как 21. В Этой версии нет страхования и разбиения очков
'''
def main():
    print('''
    Правила игры: \n
    Постаратейсь набрать макс близкое \n
    к 21 число, не привышая его. \n
    Короли, дамы, валеты приносят по 10 очков. \n
    Тузы приносят 1 или 11 очков. \n
    Карты от 2 до 10 приносят свой номинал. \n
    (H)it, чтоб взять карту. \n
    (S)stand, чтоб прекратить брать карты. \n
    (D)abell, чтоб удвоить вставку при первой игре. \n
    В случае нечьи ставка возвращается к игроку \n
    Диллер прекращает тратить карты на 17 очках \n
    ''')
    money = 5000
    while True:
        if money <= 0:
            print('''
            Ты проиграл, у тебя закончились кредиты.
            ''')
            sys.exit()
        print(f"Кредиты: {money}")
        bet = get_bet(money)
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]
        print(f"Ставка: {bet}")
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()
            if get_hand_value(player_hand) > 21:
                break
            move = get_move(player_hand, money - bet)
            if move == 'D':
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print(f"Ставка изменилась => {bet}")
            if move in ("H", "D"):
                new_card = deck.pop()
                rank, suit = new_card
                print(f"выпала карта {rank} номиналом {suit}")
                player_hand.append(new_card)
                if get_hand_value(player_hand) > 21:
                    continue
            if move in ("S", "N", "D"):
                break
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                print("Диллер берет карту")
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)
                if get_hand_value(dealer_hand) > 21:
                    break
                input("для продолжения нажмите enter...")
                print("\n\n")
        display_hands(player_hand, dealer_hand, True)
        player_value = get_hand_value(player_hand)
        dealer_value =  get_hand_value(dealer_hand)
        if dealer_value > 21:
            print(f"Диллер перебрал, выйграл ставку {bet}")
            money += bet
        elif player_value > 21 or player_value < dealer_value:
            print("Ты проиграл!")
            money -= bet
        elif player_value > dealer_value:
            print("Ты победил")
            money += bet
        elif player_value == dealer_value:
            print("Ничья, победителя нету")
        input("для продолжения нажмите enter...")
def get_bet(max_bet):
    while True:
        bet = input(f"Сколько хотите поставить от 1-{max_bet} \n"
                    "Ваш выбор").upper().strip()
        if bet == "QUIT":
            print("Выход")
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet
def get_deck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
            for rankd in "JQKA":
                deck.append((rankd, suit))
    random.shuffle(deck)
    return deck
def display_hands(player_hand, dealer_hand, show_dealer_hand):
    print()
    if show_dealer_hand:
        print(f"Диллер: {get_hand_value(dealer_hand)}")
        display_cards(dealer_hand)
    else:
        print("Диллер: ????")
        display_cards([BACKSIDE] + dealer_hand[1:])
    print(f"Игрок: {get_hand_value(player_hand)}")
    display_cards(player_hand)
def get_hand_value(cards):
    value = 0
    number_of_access = 0
    for card in cards:
        rank = card[0]
        if rank == "A":
            number_of_access += 1
        elif rank in "KQJ":
            value += 10
        else:
            value += int(rank)
    value += number_of_access
    for i in range(number_of_access):
        if value + 10 <= 21:
            value += 10
    return value
def display_cards(cards):
    rows = ['', '', '', '', '']
    for i, card in enumerate(cards):
        rows[0] += " ___ "
        if card == BACKSIDE:
            rows[1] += ' |## | '
            rows[2] += ' |###| '
            rows[3] += ' |_##| '
        else:
            rank, suit = card
            rows[1] += ' |{} | '.format(rank.ljust(2))
            rows[2] += ' | {} | '.format(suit)
            rows[3] += ' |_{}| '.format(rank.rjust(2, "_"))
    for row in rows:
        print(row)
def get_move(player_hand, money):
    while True:
        moves = ['(H)it', '(S)tand']
        if len(player_hand) == 2 and money > 0:
            moves.append('(D)ouble down')
        move_prompt = ", ".join(moves) + "> "
        move = input(move_prompt).upper()
        if move in "HS":
            return move
        if move == "D" and "(D)ouble down" in moves:
            return move
if __name__ == "__main__":
    main()
# ответы
# 1. строка 29, сначала 5000 кредитов
# 2. в 31 строке после начала цикла имеется проверка денег, если равно нулю то выходит.
# на 96 строке проверка bet с max_bet при проверке значения
# 3. в 137 строке в функции display_cards создаются строки, и далее проверяется если карта равно бэксайду
#  то выводится просто карта, или добывается переменная и создается карта через индексы.
# 4. в display_hands в начале проверяется итерация и выходит дилер, после выхода с итерации показывается игрок
#  и дальше проходится по функции display_cards
# 5. соотвествует ли карте, если бэксайд то просто карта а,
#  если с символом то его символ и буква(буква в 1 и 3, символ в 2)
# 6. во первых будет отсуствовать рандом,
# во вторых при выводе будет выведенна 2 раза карты с дилером и игороком
# 7. проигрыш будет считаться победой.
#  а когда дойдет до итерации с проверкой числа то не будет выхода из-за проигрыша.
# 8. Если передавать true то истинна первая итерация в функции и дальше выводится карты дилера.
#  Если ложь то будет выводится непонятное кол во очков и карты диллера
# '''
# --------------------------ПРАКТИКА 15------------------------------------------------------------
# '''
#1)
class animal:
    def __init__(self, nickname):
        self.nickname = nickname
    def __str__(self):
        return self.nickname
class cat(animal):
    def __init__(self, nickname):
        super().__init__(nickname)
    def voice(self):
        print("мяуууу")
    def run(self):
        print("бегу")
#класс попугая
class parrot(animal):
    def __init__(self, nickname):
        super().__init__(nickname)
    def voice(self):
        print("карррр")
    def fly(self):
        print("лечу")
#2)
#class message:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
    def zagolovok(self):
        print(f"от {self.sender} к {self.receiver}:")
class Text_message(message):
    def __init__(self, sender, receiver, text):
        super().__init__(sender, receiver)
        self.text = text
    def отправь(self):
        self.zagolovok()
        print(self.text)
class sticker_message(message):
    def __init__(self, sender, receiver, sticker):
        super().__init__(sender, receiver)
        self.sticker = sticker
        self.balance = 1
    def send(self):
        self.zagolovok()
        print(f"{self.sticker} {self.balance}")
        self.balance += 1
#3)
import random
class msdice:
    def __init__(self, грани):
        self.facets = грани
    def кинуть(self):
        return random.randint(1, self.facets)
d10 = msdice(10)
print("бросок d10:", d10.кинуть())
print("ещё раз d10:", d10.кинуть())
d20 = msdice(20)
print("бросок d20:", d20.кинуть())
print("ещё разу d20:", d20.кинуть())
#4)
class player:
    # конструктор класса
    def __init__(self, nickname):
        self.nickname = nickname
        self.exp_points = 0
        self.inventory = []
    # переопределяет строковое представление
    def __str__(self):
        return f"player {self.nickname} with {self.exp_points} exp and inventory {self.inventory}"
    # добавляет указанное количество очков опыта.
    def addexp(self, exp):
        self.exp_points += exp
    # добавляет предмет в инвентарь
    def additem(self, item):
        self.inventory.append(item)
    # удаляет предмет из инвентаря, если он есть
    def removeitem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
#5)
def parallel(r1, r2): return r1 * r2 / (r1 + r2)
def consec(resistances): return sum(resistances)
# '''
# --------------------------ПРАКТИКА 16------------------------------------------------------------
# '''
#1)
import random
lst = [random.randint(-10, 10) for _ in range(20)]
print("исходный список:", lst)
# делим список пополам
mid = len(lst) // 2
left = sorted(lst[:mid])                  # по возрастанию
right = sorted(lst[mid:], reverse=True)   # по убыванию
result = left + right
print("результат:", result)
#2)
import random
lst = [random.randint(-20, 20) for _ in range(45)]
print("исходный список:", lst)
size = len(lst) // 3
p1, p2, p3 = lst[:size], lst[size:2*size], lst[2*size:]
max_p2 = max(p2)
min_p2 = min(p2)
middle = []
for i in range(len(p2)):
    middle.append(max_p2 if i % 2 == 0 else min_p2)
result = [x for x in p1 if x % 2 == 0] + middle + [x for x in p3 if x % 2 != 0]
print("результат:", result)
# '''
# --------------------------ПРАКТИКА 17------------------------------------------------------------
# '''
from tkinter import *
tern = "X"
wins_x = 0
wins_o = 0
game_over = False
def check_win():
    global wins_x, wins_o, game_over
    lines = [
        (btn[0], btn[1], btn[2]), (btn[3], btn[4], btn[5]), (btn[6], btn[7], btn[8]),
        (btn[0], btn[3], btn[6]), (btn[1], btn[4], btn[7]), (btn[2], btn[5], btn[8]),
        (btn[0], btn[4], btn[8]), (btn[2], btn[4], btn[6])
    ]
    for a, b, c in lines:
        if a['text'] == b['text'] == c['text'] != '-':
            winner = a['text']
            lbl.configure(text=winner + " победил, молодец")
            if winner == "X":
                wins_x += 1
            else:
                wins_o += 1
            score_lbl.configure(text=f"X: {wins_x}   O: {wins_o}")
            game_over = True
            return
    # Ничья
    if all(b['text'] != '-' for b in btn):
        lbl.configure(text="ничья, эх")
        game_over = True
def clicked(i):
    global tern, game_over
    if game_over or btn[i]['text'] != '-':
        return
    btn[i].configure(text=tern)
    if tern == "X":
        tern = "0"
    else:
        tern = "X"
    check_win()
def restart():
    global tern, game_over
    tern = "X"
    game_over = False
    lbl.configure(text='')
    for b in btn:
        b.configure(text='-')
    score_lbl.configure(text=f"X: {wins_x}   O: {wins_o}")
window = Tk()
window.title("tip and toe")
window.geometry("1000x1000")
lbl = Label(window, text='', font=('Arial Bold', 50))
lbl.grid(column=0, row=0, columnspan=4)
score_lbl = Label(window, text="X: 0   O: 0", font=('Arial Bold', 30))
score_lbl.grid(column=0, row=4, columnspan=4)
restart_btn = Button(window, text="по новой", font=('Arial Bold', 20), command=restart)
restart_btn.grid(column=0, row=5, columnspan=4)
btn = [
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=0: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=1: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=2: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=3: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=4: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=5: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=6: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=7: clicked(i)),
    Button(window, text='-', font=('Arial Bold', 50), width=5, height=2, command=lambda i=8: clicked(i))
]
btn[0].grid(column=1, row=1)
btn[1].grid(column=2, row=1)
btn[2].grid(column=3, row=1)
btn[3].grid(column=1, row=2)
btn[4].grid(column=2, row=2)
btn[5].grid(column=3, row=2)
btn[6].grid(column=1, row=3)
btn[7].grid(column=2, row=3)
btn[8].grid(column=3, row=3)
window.mainloop()
#
        print(f"Значение {user_value} не найдено в списке.")
except ValueError:
    print("Некорректный ввод. Пожалуйста, введите целое")
