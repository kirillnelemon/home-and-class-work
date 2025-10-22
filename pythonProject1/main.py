from random import randint
N = 15
mylist = []
for i in range(N):
    mylist.append(randint(1, 100))
print(f"Неотсортированный список: {mylist}")
i = 0
while i < N - 1:
    m = i
    j = i + 1
    while j < N:
        if mylist[j] > mylist[m]:
            m = j
        j += 1
    mylist[i], mylist[m] = mylist[m], mylist[i]
    i += 1
print(f"Отсортированный список: {mylist}")
# import re
#
#
# def isCyrillic(text):
#     return bool(re.search('[а-яА-Я]', text))
#
#
# point_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# point_ru = {1: 'АВЕЙНОСТ', 2: 'ДКАМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗЧЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
#
# num_rounds = 10
# num_players = int(input("Введите количество игроков: "))
# scores = {i: 0 for i in range(1, num_players + 1)}
#
# for round_num in range(1, num_rounds + 1):
#     print(f"\n--- Раунд {round_num} ---")
#     for player_num in range(1, num_players + 1):
#         text_user = input(f"Игрок {player_num}, введите слово: ").upper()
#
#         if isCyrillic(text_user):
#             score = sum(key for char in text_user for key, value in point_ru.items() if char in value)
#         else:
#             score = sum(key for char in text_user for key, value in point_en.items() if char in value)
#
#         scores[player_num] += score
#         print(f"Очки за слово: {score}")
#
# print("\n--- Итоги игры ---")
# for player_num, score in scores.items():
#     print(f"Игрок {player_num}: {score} очков")
#
# backpack = {'Зажигалка': 20, 'Компас': 100, 'Фрукты': 500, 'Рубашка': 300, 'Термос': 1000, 'Аптечка': 200, 'Куртка': 600, 'Бинокль': 400, 'Удочка': 1300, 'Салфетки': 40, 'Бутерброды': 800, 'Палатка': 5500, 'Спальный мешок': 2500, 'Изолента': 250, 'Котел': 3000}
# massa = int(input("Введите допустимый вес рюкзака: ")) * 1000
#
# print("Могу взять: ")
# for key, value in backpack.items():
#     if value < massa:
#         print(key, value, end=' ')
# print()
#
# print("Не Могу взять: ")
# for key, value in backpack.items():
#     if value > massa:
#         print(key, value, end=' ')

#Задание №4
words = ["apple", "banana", "cherry", "date", "apricot"]
words.sort()
print(words)
for i in range(len(words)):
    min_ind = i
    for j in range(i + 1, len(words)):
        if words[j] < words[min_ind]:
            min_ind = j
    words[i], words[min_ind] = words[min_ind], words[i]
print(words)
# note_book = {
# "Маша": ('tel:+7922123561', 'vk:vk.com/masha321', 'youtube:youtube.com/masha321', 'telegram:t.me/masha321')
#         }
#
# user_search = input("Введите имя из списка контактов:").capitalize()
# if user_search in note_book:
#     contact_info = note_book[user_search]
#     print(f"Имя: {user_search}")
#     print(f"Телефон: {contact_info[0]}")
#     print(f"ВК: {contact_info[1]}")
#     print(f"Ютуб: {contact_info[2]}")
#     print(f"Телеграм: {contact_info[3]}")
# else:
#     print("Контакт не найден.")