# config.py

archer = { #Лучник
    "hp": 50,
    'speed': 70, #Скорость,
    'intelligence': 5, #интеллект,
    'power': 10, #сила,
    'agility': 15, #ловкость,
    'lucky': 15, #удача,
    'power_damage': 15, #сила атаки,
    'exp': 0 #опыт,
}

warrior = { #Воин
    "hp": 100,
    'speed': 30, #Скорость,
    'intelligence': -3, #интеллект,
    'power': 25, #сила,
    'agility': 3, #ловкость,
    'lucky': 10, #удача,
    'power_damage': 50, #сила атаки,
    'exp': 0 #опыт,
}

mage = { #Маг
    "hp": 50,
    'speed': 50, #Скорость,
    'intelligence': 25, #интеллект,
    'power': 1, #сила,
    'agility': 5, #ловкость,
    'lucky': 10, #удача,
    'power_damage': 70, #сила атаки,
    'exp': 0 #опыт,
}

tank = { #Танк
    "hp": 150,
    'speed': 10, #Скорость,
    'intelligence': 1, #интеллект,
    'power': 50, #сила,
    'agility': 1, #ловкость,
    'lucky': 1, #удача,
    'power_damage': 20, #сила атаки,
    'exp': 0 #опыт,
}

# Пустые словари для заклинаний
mage_spells = {}
tank_spells = {}
archer_spells = {}
warrior_spells = {}

# Враги
slime = {"name":"slime","damage":2, "hp":50, "protection":0}
goblin = {"name":"goblin","damage":6, "hp":150, 'protection': 10}
orc = {"name":"orc","damage":10, "hp":250, 'protection': 20}
spectator = {"name":"spectator","damage":50, "hp":1050, 'protection': 50}

# Список врагов
enemy_list = [slime, goblin, orc, spectator]