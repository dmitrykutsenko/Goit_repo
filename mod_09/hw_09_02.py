'''
Implement the function get_discount_price_customer to calculate the price of an online store product, taking into account the customer's discount.

The function accepts two parameters:

     price — product price
     customer — a dictionary with customer data of the following type: {"name": "Dima"} or {"name": "Boris", "discount": 0.15}

You have a global variable DEFAULT_DISCOUNT that defines the discount for the customer if they don't have a discount field.

The get_discount_price_customer function should return the new product price for the customer.

We will remind you that a discount is a fractional number from 0 to 1. And we understand a discount as a coefficient that determines the value of the price. And by this value, we reduce the final price of the product: price = price * (1 - discount).
'''

DEFAULT_DISCOUNT = 0.05

def get_discount_price_customer(price, customer):
    # get the discount value for the customer, or the default value if not found
    discount = customer.get("discount", DEFAULT_DISCOUNT)
    # calculate the new price by applying the discount formula
    new_price = price * (1 - discount)
    # return the new price
    return new_price