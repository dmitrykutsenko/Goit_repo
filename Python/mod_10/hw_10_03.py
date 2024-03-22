'''
А тепер до цього прикладу реалізуйте в класі Animal метод change_weight, який має змінювати вагу тварини.
Викличте функцію change_weight(12) для об'єкта animal та змініть значення початкової ваги з 10 на 12 одиниць.
'''

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, new_weight):
        self.weight = new_weight

# Створення екземпляра класу Animal
animal = Animal(nickname="Fluffy", weight=10)

# Доступ до властивостей екземпляра
print(f"Nickname: {animal.nickname}")
print(f"Weight: {animal.weight}")

# Виклик методу change_weight для зміни ваги
animal.change_weight(12)

# Перевірка зміни ваги
print(f"New Weight: {animal.weight}")
