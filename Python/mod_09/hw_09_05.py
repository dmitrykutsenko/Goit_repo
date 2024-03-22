'''
Маємо Python функцію
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

Треба зробити для неї декоратор
def format_phone_number(func):

який буде замість таких результатів:
380501233234
0503451234
0508889900
380501112222
380501112211

давати їх у іншому форматі, а саме:

+380501233234
+380503451234
+380508889900
+380501112222
+380501112211

Отже, вказаний декоратор повинен додавати для коротких номерів префікс +38, а для повного міжнародного номера (з 12 символом) - тільки знак +. Реалізуйте декоратор format_phone_number для функції sanitize_phone_number з необхідним функціоналом.
'''

# define the decorator function
def format_phone_number(func):
    def wrapper(phone):
        new_phone = func(phone)
        if len(new_phone) == 10:
            new_phone = "+38" + new_phone
        elif len(new_phone) == 12:
            new_phone = "+" + new_phone
        return new_phone
    return wrapper


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone