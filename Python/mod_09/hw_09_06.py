'''
Нехай є рядок з числами (з метою спрощення числа лише цілі), що визначає якісь частини загального доходу. Наприклад,

"The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."

Необхідно реалізувати функцію generator_numbers, яка буде парсити рядок і знаходити всі цілі числа в ньому та працювати як генератор, який буде віддавати зазначені числа при зверненні до нього у циклі.

    З парсингом рядків ми вже зіштовхувалися виконуючи завдання модуля 7, коли розбивали на лексеми арифметичний вираз

Функція generator_numbers(string="") безпосередньо розпарсює рядок і за допомогою yield повертає поточне число.

Функція sum_profit(string) підсумовує числа, отримані від generator_numbers, та повертає загальну суму прибутку з рядка.
'''

import re

def generator_numbers(string=""):
    # Using regular expression to find all integers in the string
    pattern = r'\b\d+\b'
    numbers = re.findall(pattern, string)

    # Yield each number found
    for num in numbers:
        yield int(num)
        
def sum_profit(string):
    # Get the generator for numbers
    numbers_generator = generator_numbers(string)

    # Sum the numbers using the generator
    total_profit = sum(numbers_generator)

    return total_profit
    
# Example usage:
input_string = "The resulting profit was: from the southern possessions $100, from the northern colonies $500, and the king gave $1000."
result = sum_profit(input_string)

print(f'Total Profit: ${result}')