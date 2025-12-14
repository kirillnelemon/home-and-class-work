
from Hero import Hero
from enemy import Enemy

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