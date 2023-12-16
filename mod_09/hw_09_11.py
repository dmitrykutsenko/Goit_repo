'''
Для списку numbers підрахувати суму елементів за допомогою функції reduce.

numbers = [3, 4, 6, 9, 34, 12]

Створіть функцію sum_numbers(numbers), результатом виконання якої буде сума чисел всіх елементів списку numbers.
'''

from functools import reduce

def sum_numbers(numbers):
    # Use reduce to calculate the sum of the elements
    result = reduce(lambda x, y: x + y, numbers, 0)
    return result

# Example usage:
numbers = [3, 4, 6, 9, 34, 12]
result = sum_numbers(numbers)

print(result)

