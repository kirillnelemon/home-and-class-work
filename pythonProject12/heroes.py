# heroes.py

class Hero:
    def __init__(self, lvl, name, last_name, lor, history, hp, old, spells, radius, weaknesses, speed, intelligence, power, agility, lucky, power_damage, exp):
        self.lvl = lvl
        self.name = name
        self.last_name = last_name
        self.lor = lor
        self.history = history
        self.hp = hp
        self.old = old
        self.spells = spells
        self.radius = radius
        self.weaknesses = weaknesses
        self.gender = None
        self.attr = {
            'speed': speed,
            'intelligence': intelligence,
            'power': power,
            'agility': agility,
            'lucky': lucky,
            'power_damage': power_damage,
            'exp': exp,
            'hp': hp
        }

    def attack_to_damage(self):
        return self.attr['power_damage']

    def protection_to_damage(self, incoming_damage):
        actual_damage = max(0, incoming_damage - self.attr.get('protection', 0))
        self.attr['hp'] -= actual_damage
        return actual_damage