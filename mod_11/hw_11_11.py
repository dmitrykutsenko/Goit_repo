'''
реалізувати клас RandomVectors, який зможе створювати об'єкт, що ітерується, і дозволяти ітеруватися по випадковим векторам.

Формат класу:

RandomVectors(max_vectors: int, max_points: int) -> Iterable(max_vectors, max_points)

де:

    max_vectors — визначає максимальну кількість елементів (примірників класу Vector) в ітерованій послідовності
    max_points — визначає максимальне значення для координат x та y (в діапазоні 0...max_points)

Щоб екземпляри класу RandomVectors були об'єктами, що ітеруються, в класі повинен бути реалізований метод __iter__, який повертає ітератор. Ітератор – це будь-який об'єкт, який на кожному кроці ітерації (крок ітерації – це виклик методу next() для цього ітератора) повертає таке значення - і так до вичерпання кількості ітерацій (визначається параметром max_vectors).

У нашому випадку ітератором буде клас Iterable, у якому необхідно реалізувати метод __next__. Він у конструкторі отримує ті ж параметри max_vectors та max_points, що і клас RandomVectors.

Метод __next__ повинен видавати кожне наступне значення зі списку self.vectors. Створіть у конструкторі набір випадкових векторів self.vectors завдовжки max_vectors за допомогою randrange. Атрибут current_index вказівник-індекс на поточний вектор зі списку vectors, необхідний для ітерування.

Приклад роботи класу `RandomVectors:

vectors = RandomVectors(5, 10)

for vector in vectors:
    print(vector)

Вивід має бути схожим на цей:

Vector(7,7)
Vector(0,0)
Vector(8,9)
Vector(1,9)
Vector(6,6)
'''

from random import randrange

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

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, (int, float)):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
            self.coordinates.x * vector.coordinates.x
            + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, vector):
        return self.len() == vector.len()

    def __ne__(self, vector):
        return self.len() != vector.len()

    def __lt__(self, vector):
        return self.len() < vector.len()

    def __gt__(self, vector):
        return self.len() > vector.len()

    def __le__(self, vector):
        return self.len() <= vector.len()

    def __ge__(self, vector):
        return self.len() >= vector.len()


class Iterable:
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.vectors = []
        for _ in range(max_vectors):
            x = randrange(max_points + 1)
            y = randrange(max_points + 1)
            self.vectors.append(Vector(Point(x, y)))

    def __next__(self):
        if self.current_index < len(self.vectors):
            current_vector = self.vectors[self.current_index]
            self.current_index += 1
            return current_vector
        else:
            raise StopIteration


class RandomVectors:
    def __init__(self, max_vectors=10, max_points=50):
        self.max_vectors = max_vectors
        self.max_points = max_points

    def __iter__(self):
        return Iterable(self.max_vectors, self.max_points)


# Example usage:

vectors = RandomVectors(5, 10)

for vector in vectors:
    print(vector)

