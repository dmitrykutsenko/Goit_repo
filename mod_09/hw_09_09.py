'''
Дякую дуже! Потрібно розв' язати наступну задачку на пайтоні. 
Є список payment з додатними та від'ємними значеннями. Створіть функцію positive_values та за допомогою функції filter відфільтруйте список payment за додатними значеннями, та поверніть його з функції.

payment = [100, -3, 400, 35, -100]

'''

def positive_values(list_payment):
    # Use filter to keep only positive values
    positive_payments = list(filter(lambda x: x > 0, list_payment))
    return positive_payments

# Example usage:
payments = [100, -3, 400, 35, -100]
result = positive_values(payments)

print(result)
