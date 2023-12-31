'''
У класу Point через конструктор __init__ оголошено два атрибути: координати x та y. Приховати доступ до них з допомогою подвійного підкреслення: __x та __y

Реалізуйте для класу Point механізми setter та getter до атрибутів __x та __y за допомогою декораторів property та setter.

Приклад:

point = Point(5, 10)

print(point.x)  # 5
print(point.y)  # 10
'''

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

# Example usage:

# Create an instance of the Point class
point = Point(5, 10)

# Access the x and y attributes using the getters
print(point.x)  # Output: 5
print(point.y)  # Output: 10

# Update the x and y attributes using the setters
point.x = 8
point.y = 15

# Access the updated x and y attributes using the getters
print(point.x)  # Output: 8
print(point.y)  # Output: 15
