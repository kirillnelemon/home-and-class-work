# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"Меня зовут {self.name},"
#               f"мне {self.age} лет")
#
# class Shape:
#     def __init__(self, name):
#         self.name = name
#     def area(self):
#         pass
#     def fact(self):
#         return "I am two-dimensional shape"
#     def __str__(self):
#         return self.name
#
# def Square(Shape):
#     def __init__(self, length):
#         super().__init__("Square")
#         self.length = length
#     def area(self):
#         return self.length**2
#     def fact(self):
#         return "Squares have each agle equal to 90 degress"
#
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius
#     def area(self):
#         return pi*self.radius**2
# #MAIN
# a = Square(4)
# b = Circle(7)
# for fig in (a,b):
#     print(fig)
#     print(fig.fact())
#     print(fig.area())

#№3