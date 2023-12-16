'''
створіть клас Animal. Також створіть екземпляр класу Animal та привласніть змінній animal. 
Для класу Animal у конструкторі створіть дві властивості: nickname - кличка тварини та weight - вага тварини. Реалізуйте також метод класу say. 
При реалізації методу можна використати оператор pass, поки що головне - це визначення, а не конкретна реалізація.
'''

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

# Create an instance of the Animal class
animal = Animal(nickname="Fluffy", weight=10)

# Accessing properties of the instance
print(f"Nickname: {animal.nickname}")
print(f"Weight: {animal.weight}")

# Calling the say method (which currently does nothing)
animal.say()
