# Нова задачка по Python coding. Є іменований кортеж для зберігання котів у змінній Cat. На першому місці у нас кличка котика nickname, потім його вік age та ім'я власника кота owner.
#
# Напишіть функцію convert_list(cats), яка працюватиме у двох режимах.
#
# Режим 1:
# Якщо функція convert_list приймає у параметрі cats список іменованих кортежів
#
#[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
#
# То функція поверне наступний список словників:
#
#[
#    {"nickname": "Mick", "age": 5, "owner": "Sara"},
#    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#    {"nickname": "Simon", "age": 3, "owner": "Yura"},
#]
#
# Режим 2:
# І в той же час, якщо функція convert_list приймає в параметрі cats список словників, то результатом буде зворотна операція та функція має повернути список іменованих кортежів.
#
# Для визначення типу параметра cats використовуйте функцію isinstance.

# Import the collections module
import collections

# Define a named tuple for storing cats
Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

# Define a function to convert a list of cats
def convert_list(cats):
    # Check if the cats parameter is a list of named tuples
    if isinstance(cats[0], Cat):
        # Create an empty list to store the dictionaries
        dicts = []
        # Loop through each named tuple in the list
        for cat in cats:
             # Convert the named tuple to a dictionary using the _asdict method
            cat_dict = cat._asdict()
            # Append the dictionary to the list
            dicts.append(cat_dict)
        # Return the list of dictionaries
        return dicts
    # Check if the cats parameter is a list of dictionaries
    elif isinstance(cats[0], dict):
    # Create an empty list to store the named tuples
        tuples = []
        # Loop through each dictionary in the list
        for cat in cats:
            # Convert the dictionary to a named tuple using the Cat function
            cat_tuple = Cat(**cat)
            # Append the named tuple to the list
            tuples.append(cat_tuple)
            # Return the list of named tuples
        return tuples
    # Otherwise, return an error message
    else:
        return "Invalid input"