'''
Додамо в клас Animal змінну класу color, значення якої спочатку дорівнює 'white', і метод change_color, який повинен змінювати значення змінної класу color.

Створіть екземпляри об'єкта: first_animal та second_animal

Викличте функцію change_color("red") для будь-якого екземпляра об'єкту Animal та змініть значення змінної класу color на "red".

'''

class Animal:
    # Class attribute
    color = 'white'

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, new_weight):
        self.weight = new_weight

    @classmethod
    def change_color(cls, new_color):
        # Accessing class attribute using cls
        cls.color = new_color

# Create object instances
first_animal = Animal(nickname="Fluffy", weight=10)
second_animal = Animal(nickname="Whiskers", weight=8)

# Accessing initial properties of the instances
print(f"First Animal - Initial Color: {first_animal.color}")
print(f"Second Animal - Initial Color: {second_animal.color}")

# Call the change_color method on the class to change the color for all instances
Animal.change_color("red")

# Accessing properties after color change
print(f"First Animal - New Color: {first_animal.color}")
print(f"Second Animal - New Color: {second_animal.color}")

