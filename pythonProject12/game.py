# game.py

from heroes import Hero
import config
from enemy import Enemy
from log import Log
import random

# Глобальные переменные для хранения данных, собранных в menu()
global_change_user = 0
global_name = ""
global_last_name = ""
global_lor = ""
global_history = ""
global_old = 0
global_weaknesses = ""

def menu():
    listTextMenu = [
        "Привет, дорогой Друг!\n",
        "Добро пожаловать в нашу игру!",
        "Желаю тебе приятно провести время!",
        "Всего у нас 4 игровых персонажа:",
        "\n\t 1. Маг \n\t 2. Танк\n\t 3. Воин \n\t 4. Лучник"
    ]
    for line in listTextMenu:
        print(line)

    global global_change_user, global_name, global_last_name, global_lor, global_history, global_old, global_weaknesses
    global_change_user = int(input("Введите число, для выбора своего класса: "))
    global_name = input("Введите имя: ")
    global_last_name = input("Введите прозвище: ")
    global_lor = input("Введите лор персонажа: ")
    global_history = input("Введите историю персонажа: ")
    global_old = int(input("Введите возраст: "))
    global_weaknesses = input("Введите страхи персонажа: ")

def battler():
    # Используем глобальные переменные
    change_user = global_change_user
    name = global_name
    last_name = global_last_name
    lor = global_lor
    history = global_history
    old = global_old
    weaknesses = global_weaknesses

    hero_class = {}
    spells = {}
    if change_user == 1:
        hero_class = config.mage
        spells = config.mage_spells
    elif change_user == 2:
        hero_class = config.tank
        spells = config.tank_spells
    elif change_user == 3:
        hero_class = config.warrior
        spells = config.warrior_spells
    elif change_user == 4:
        hero_class = config.archer
        spells = config.archer_spells
    else:
        print("Неверный выбор. Создаём Мага по умолчанию.")
        hero_class = config.mage
        spells = config.mage_spells

    hero = Hero(
        lvl=1,
        name=name,
        last_name=last_name,
        lor=lor,
        history=history,
        hp=hero_class["hp"],
        old=old,
        spells=spells,
        radius=1,
        weaknesses=weaknesses.split(',') if weaknesses else [],
        speed=hero_class["speed"],
        intelligence=hero_class["intelligence"],
        power=hero_class["power"],
        agility=hero_class["agility"],
        lucky=hero_class["lucky"],
        power_damage=hero_class["power_damage"],
        exp=hero_class["exp"]
    )

    # Начинаем с первого врага — Слизи
    enemy = Enemy(config.slime)
    log = Log(1, hero.name)
    hero_damage_menu_battle(hero, enemy, log)


def hero_damage_menu_battle(hero, enemy, log):
    enemy_list = config.enemy_list
    current_enemy_index = 0  # Начинаем со слизи

    while True:
        # Проверка на победу над текущим врагом
        if enemy.attr['hp'] <= 0:
            log.victory_lvl()
            current_enemy_index += 1
            if current_enemy_index >= len(enemy_list):
                print(" Все враги побеждены! Игра пройдена!")
                Log.show_stats()
                break
            # Берём следующего врага
            enemy = Enemy(enemy_list[current_enemy_index])
            print(f"\n➡ Появился новый враг: {enemy.attr['name']}!")

        # Проверка на смерть героя
        if hero.attr['hp'] <= 0:
            log.faild_lvl()
            Log.show_stats()
            break

        # Боевые действия
        hero_damage = hero.attack_to_damage()
        enemy.protection_to_damage(hero_damage)
        log.damage(hero.name, hero_damage)

        if enemy.attr['hp'] > 0:  # Только если враг ещё жив
            enemy_damage = enemy.attack_to_damage()
            hero.protection_to_damage(enemy_damage)
            log.damage(enemy.attr['name'], enemy_damage)