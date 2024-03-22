def cost_delivery(quantity, *_, discount = 0):
    init_price = 5
    next_price = 2
    subtotal = 0
    for each in range(1, int(quantity)+1):  
        print(str(each))      
        if each == 1:
            subtotal = init_price
        else:   
            subtotal = subtotal + next_price

    total = subtotal * (1 - discount)
    
    return(total)

print(str(cost_delivery(2, 1, 2, 3)))

def cost_deliver2y(quantity, *_, discount=0):
    """Функція повертає суму за доставлення замовлення.

     Перший параметр &mdash; кількість товарів в замовленні.
     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""

    
    
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result
