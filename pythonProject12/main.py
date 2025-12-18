<<<<<<< HEAD
from tkinter import *
=======
>>>>>>> 067486d503d5aabf9a0da4a83e09b06a01d59a61

from Hero import Hero
from enemy import Enemy

<<<<<<< HEAD

window = Tk()
window.title("Добро пожаловать в мое приложение!")#титульник
window.mainloop()#бесконечный цикл
=======
# Пример создания героя
hero = Hero(
    name="Алиса",
    last_name="Молния",
    lor="Из леса Туманов",
    history="Орден Звёздных Стражей",
    hp=100,
    old=18,
    spells=["Огненный шар", "Щит"],
    radius=5,
    weaknesses=["Яд"],
    speed=8,
    intelligence=10,
    power=6,
    lucky=7,
    agility=9,
    power_damage=15,
    exp=0
)

print(f"Создан герой: {hero.name} {hero.last_name}")
>>>>>>> 067486d503d5aabf9a0da4a83e09b06a01d59a61
