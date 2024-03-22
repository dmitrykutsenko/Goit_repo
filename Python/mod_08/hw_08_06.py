# Створіть функцію decimal_average(number_list, signs_count), яка обчислюватиме середнє арифметичне типу Decimal з кількістю значущих цифр signs_count. Параметр number_list — список чисел
# 
# Не забувайте приводити всі числа у списку до типу `decimal`
#
# Приклад:
#    виклик функції decimal_average([3, 5, 77, 23, 0.57], 6) поверне 21.714
#    виклик функції decimal_average([31, 55, 177, 2300, 1.57], 9) поверне 512.91400

# by Alex
#from decimal import Decimal, getcontext
#def decimal_average(number_list, signs_count):
#    getcontext().prec = signs_count
#    decimal_numbers = [Decimal(x) for x in number_list]
#    total = sum(decimal_numbers)
#    average = total/ Decimal(len(decimal_numbers))
#    return(average)

#by "me"

# Import the decimal module
from decimal import Decimal, getcontext

# Define a function to calculate the decimal average
def decimal_average(number_list, signs_count):
    # Convert all numbers in the list to decimal type using the map function
    number_list = list(map(Decimal, number_list))
    # Calculate the sum of the numbers using the sum function
    total = sum(number_list)
    # Calculate the length of the list using the len function
    length = len(number_list)
    # Calculate the average by dividing the total by the length
    average = total / length
    # Normalize the average to remove any trailing zeros using the normalize method
    average = average.normalize()
    # Convert the average to a string using the str function
    str_average = str(average)
    # Find the position of the decimal point using the find method
    point = str_average.find('.')
    # Slice the string to keep only the given number of significant digits after the decimal point
    str_average = str_average[:point + signs_count + 1]
    # Convert the string back to a decimal type using the decimal.Decimal function
    average = Decimal(str_average)
    # Return the average
    #return(average)
    print(average)


decimal_average([4.5788689699797, 34.7576578697964, 86.8877666656633, 12], 6) 
#decimal_average([4.5788689699797, 34.7576578697964, 86.8877666656633, 12])
#decimal_average([3, 5, 77, 23, 1.33543546])
#decimal_average([4, 15, 1.77, 23, 1.33543546, 7, 89])
