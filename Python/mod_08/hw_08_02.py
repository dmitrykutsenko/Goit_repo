#Напишіть функцію визначення кількості днів у конкретному місяці.
#Ваша функція повинна приймати два параметри: month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12 
#і year - рік, що складається із чотирьох цифр. Перевірте, чи функція коректно обробляє місяць лютий високосного року.

# write a Python function that will determine the number of days in a particular month. The function must accept two parameters: month - the number of the month in the form of an integer in the range from 1 to 12, and year - the year consisting of four digits. You also want me to check that the function correctly handles the month of February in a leap year. Here is the code I wrote:
from datetime import date
# Define a function to determine the number of days in a month
def get_days_in_month(month, year):
    # Check if the month and year are valid
    if not (1 <= month <= 12 and 1000 <= year <= 9999):
        return "Invalid input"
    # Create a list of the number of days in each month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Check if the year is a leap year and adjust the number of days in February
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29
    # Return the number of days in the given month 
    return days_in_month[month - 1]


# Test the function with some examples
print(get_days_in_month(2, 2020)) # Output: 29
print(get_days_in_month(2, 2021)) # Output: 28
print(get_days_in_month(4, 2023)) # Output: 30
print(get_days_in_month(12, 2025)) # Output: 31
print(get_days_in_month(13, 2026)) # Output: Invalid input