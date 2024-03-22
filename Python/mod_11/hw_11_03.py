'''
У класу Point до механізму setter властивостей x і y додайте перевірку на значення, що вводиться. Дозвольте встановлювати значення властивостей x та y для екземпляра класу, тільки якщо вони мають числове значення (int або float).

Приклад:

point = Point("a", 10)

print(point.x)  # None
print(point.y)  # 10
'''
'''
class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x
        else:
            print("Invalid value for x. Please provide a numeric value.")
            self.__x = None

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, (int, float)):
            self.__y = y
        else:
            print("Invalid value for y. Please provide a numeric value.")
            self.__y = None

# Example usage:

# Create an instance of the Point class with invalid values for both x and y
point = Point("a", "b")

# Access the x and y attributes using the getters
print(point.x)  # Output: None
print(point.y)  # Output: None
'''

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if type(x) in (int, float):
            self.__x = x
        else:
            print("Invalid value for x. Must be an integer or float.")
            self.__x = None
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if type(y) in (int, float):
            self.__y = y
        else:
            print("Invalid value for y. Must be an integer or float.")
            self.__y = None

# Example usage:

# Create an instance of the Point class with invalid values for both x and y
point = Point("a", "b")

# Access the x and y attributes using the getters
print(point.x)  # Output: None
print(point.y)  # Output: None
