'''
Для підходу із позиції карування функцій в пайтоні створіть функцію discount_price(discount), яка визначатиме в собі та повертатиме функцію розрахунку реальної ціни з урахуванням знижки.

Виклик функції discount_price(discount) поверне функцію, яка розраховує ціну на товар зі знижкою, що дорівнює discount .

Наприклад, код:

cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))

Повинен вивести:

85.0
90.0
95.0
'''

def discount_price(discount):
    # define a nested function that calculates the discounted price
    def actual_price(price):
        # apply the discount formula
        return price * (1 - discount)
    # return the nested function
    #return actual_price
    print(actual_price)

price = 100
cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))