"""
Треба зробити два класи: CatDog та DogCat. Ці класи повинні наслідуватись від двох класів відразу: Cat та Dog. 
Після успадкування в екземпляра класу CatDog, батьківський метод say повинен повертати "Meow", а у класу DogCat — "Woof". 
Для обох зазначених класів реалізуйте метод info, який повертає рядок у наступному форматі f"{self.nickname}-{self.weight}".
"""

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def info(self):
        return f"{self.nickname}-{self.weight}"


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):
    def say(self):
        return super().say()  # Call the say method from Cat class


class DogCat(Dog, Cat):
    def say(self):
        return super().say()  # Call the say method from Dog class


# Example usage:

# Create an instance of CatDog
cat_dog_instance = CatDog(nickname="CattyDoggy", weight=15)
print(f"CatDog Sound: {cat_dog_instance.say()}")
print(f"CatDog Info: {cat_dog_instance.info()}")

# Create an instance of DogCat
dog_cat_instance = DogCat(nickname="DoggyCatty", weight=20)
print(f"DogCat Sound: {dog_cat_instance.say()}")
print(f"DogCat Info: {dog_cat_instance.info()}")
