class Human:
    def __init__(self, name, eyes_color, blood_type, occupation):
        # Публичные свойства (наследуются)
        self.name = name
        self.eyes_color = eyes_color
        self.blood_type = blood_type

        # Приватное свойство (не наследуется напрямую, инкапсуляция)
        # Доступно только внутри этого класса
        self.__occupation = occupation

    def get_occupation(self):
        return f"Профессия: {self.__occupation}"


class Parent(Human):
    def __init__(self, name, eyes_color, blood_type, occupation, savings):
        super().__init__(name, eyes_color, blood_type, occupation)
        # Свойство, которое не должно передаваться автоматически (защищенное)
        self._savings = savings


class Child(Parent):
    def __init__(self, name, mother, father):
        # Ребенок наследует цвет глаз от матери, а группу крови от отца
        super().__init__(
            name=name,
            eyes_color=mother.eyes_color,
            blood_type=father.blood_type,
            occupation="Student",
            savings=0
        )


# Создаем объекты (родители)
mom = Parent("Анна", "Голубые", "A(II)", "Инженер", 50000)
dad = Parent("Иван", "Карие", "B(III)", "Врач", 70000)

# Создаем объект потомка
kid = Child("Алексей", mom, dad)

# Демонстрация
print(f"Ребенок {kid.name}:")
print(f"- Цвет глаз (от матери): {kid.eyes_color}")
print(f"- Группа крови (от отца): {kid.blood_type}")
