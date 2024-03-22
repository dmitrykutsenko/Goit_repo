'''
Cтворити клас CatDog, не використовуючи успадкування від класу Animal, 
але щоб екземпляр класу CatDog поводився як і, як екземпляр класу Cat, тобто. він повинен вдати, що він клас Cat.
'''

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

class Cat(Animal):
    def say(self):
        return "Meow"

class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
        self.cat_instance = Cat(nickname, weight)

    def say(self):
        return self.cat_instance.say()

    def change_weight(self, weight):
        self.cat_instance.change_weight(weight)
        self.weight = weight

# Example usage:

# Create an instance of CatDog
cat_dog_instance = CatDog(nickname="CatDoggy", weight=15)

# Accessing the nickname, weight, and behaving like a Cat instance
print(f"CatDog Nickname: {cat_dog_instance.nickname}")
print(f"CatDog Weight: {cat_dog_instance.weight}")
print(f"CatDog Sound: {cat_dog_instance.say()}")

# Change weight as if it's a Cat
cat_dog_instance.change_weight(20)

# Behave like a Cat instance after weight change
print(f"CatDog Weight: {cat_dog_instance.weight}")
print(f"CatDog Sound: {cat_dog_instance.say()}")
