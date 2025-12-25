#"задание 1"
famnameot4estwo = input("введите фамилию имя очество")
adres = input("введите свой адрес")
age = int(input("введите свой возраст"))
age2 = int(input("введите свой год рождения"))
print(f"ваше ФИО: {famnameot4estwo } ваш адрес {adres} ваш возраст: {age} ваш год рождения: {age2}")
#задание 2
uwle4henia =["football","backetball","gaming","ride a bike", "play hockey", "watch tv", "watcg tiktok", "play with friends", "study", "sleep"]
for i in uwle4henia:
    print(i)
print("*"*11)
predmeti = {1:"математика",2:"русский",3:"Литра", 4:"физика", 5:"английский", 6:"ОИТ", 7:"итоговый проект", 8:"информатика", 9:"введение в специальность", 10:"биология", 11:"история", 12:"введение в язык програмирования в пайтон"}
for key,value in predmeti.items():
    print(key,value)

file_name = "test.txt"
with open(file_name, 'w' ,encoding='utf-8') as f:
    for key,value in predmeti.items():
        f.write(f"{key}{value} \n")

    print("класс успешно записан!")
class Student:
    def __init__(self, famnameot4estwo, adres, age, age2,):
        self.famnameot4eswo = famnameot4estwo
        self.adres = adres
        self.age = age
        self.age2 = age2
    def printf(self):
