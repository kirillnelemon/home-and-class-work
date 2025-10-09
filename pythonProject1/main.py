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
