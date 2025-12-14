# enemy.py

class Enemy:
    def __init__(self, attr):
        self.attr = attr

    def attack_to_damage(self):
        return self.attr['damage']

    def protection_to_damage(self, incoming_damage):
        actual_damage = max(0, incoming_damage - self.attr.get('protection', 0))
        self.attr['hp'] -= actual_damage
        return actual_damage