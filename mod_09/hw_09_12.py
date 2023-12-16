'''
3 допомогою функції reduce попрацюємо з платежами.

payment = [1, -3, 4]

def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum

Нагадаємо умову. У нас є список показань заборгованостей з комунальних послуг наприкінці місяця. 
Заборгованості можуть бути від'ємними — у нас переплата, чи додатними, якщо необхідно сплатити за рахунками.
За допомогою reduce підсумуйте додатні значення та поверніть з функції amount_payment суму платежу в кінці місяця.

'''

from functools import reduce

def amount_payment(payment):
    # Use reduce to calculate the sum of the elements
    result = reduce(lambda x, y: max(x, 0) + max(y, 0), payment, 0)
    return result

# Example usage:
numbers = [3, 4, 6, 9, 34, 12]
result = amount_payment(numbers)

numbers2 =  [100, -3, 400, 35, -100]
result2 = amount_payment(numbers2)

print(result)
print(result2)
