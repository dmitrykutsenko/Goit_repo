'''
Створіть клас NumberString, успадкуйте його від класу UserString, 
визначте для нього метод number_count(self), який буде рахувати кількість цифр у рядку.
'''

from collections import UserString

class NumberString(UserString):
    def number_count(self):
        return sum(char.isdigit() for char in self.data)

# Example usage:

# Create an instance of NumberString
number_string = NumberString("Hello123World456")

# Call the number_count method to count the number of digits
digit_count = number_string.number_count()
print(f"Number of Digits: {digit_count}")

