"""
Треба зробити клас LookUpKeyDict, батьком якого буде клас UserDict. Зробіть функцію lookup_key методом класу LookUpKeyDict. 

Можна також врахувати, що маючи функцію lookup_key, вона потрібна для пошуку всіх ключів за значенням у словнику. 
Першим параметром у функцію ми можемо передавати словник, а другим – значення, яке хочеться знайти. 
Результатом є список ключів або порожній список, якщо ми нічого не знаходили.

def lookup_key(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)
    return keys
"""

from collections import UserDict

class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys

# Example usage:

# Create an instance of LookUpKeyDict
lookup_dict = LookUpKeyDict({'a': 1, 'b': 2, 'c': 1, 'd': 3})

# Call the lookup_key method to find keys for a given value
result_keys = lookup_dict.lookup_key(1)
print(f"Keys for value 1: {result_keys}")

result_keys_not_found = lookup_dict.lookup_key(4)
print(f"Keys for value 4: {result_keys_not_found}")
