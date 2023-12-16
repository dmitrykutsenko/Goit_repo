'''
Створіть клас Cat, батьківським класом якого є клас Animal. У класі Cat виконайте перевизначення методу say, щоб він повертав рядок "Meow" для екземплярів класу Cat.

Фактично ми виконуємо при цьому поліморфізм. Поліморфізм - це здатність програми вибирати різні реалізації при виклику операцій з однією і тією ж назвою. Тобто при виклику методу say в екземпляра класу Cat викликається нова реалізація, а не успадкована від класу Animal

Створіть також змінну cat, яка буде екземпляром класу Cat. При створенні змінної cat ім'я кота має бути "Simon", а вага - 10 одиниць.
'''

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return "Generic animal sound"

    def change_weight(self, new_weight):
        self.weight = new_weight


class Cat(Animal):
    def say(self):
        return "Meow"

# Create an instance of the Cat class
cat = Cat(nickname="Simon", weight=10)

# Accessing properties and methods of the Cat instance
print(f"Cat Name: {cat.nickname}")
print(f"Cat Weight: {cat.weight}")
print(f"Cat Sound: {cat.say()}")
