from datetime import datetime, timedelta

def outer(x):
    def inner(y):
        return x + y
    return inner


add_five = outer(5)
#print(add_five(3))
#print(add_five(10))

#datetime.today().date()
print(str(datetime.strptime("2001-01-01", "%Y-%m-%d").date()))