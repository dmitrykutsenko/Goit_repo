'''
Для ситуацій, коли нам потрібно, щоб на будь-якому рівні вкладеності створювалися нові об'єкти, 
а не посилання на ті що існують, у пакеті copy є функція deepcopy. Ця функція створює рекурсивно нові об'єкти.

import copy

my_list = [1, 2, {1: 'a'}]
copy_list = copy.deepcopy(my_list)
copy_list.append(4)
print(my_list)  # [1, 2, {1: 'a'}]
print(copy_list)  # [1, 2, {1: 'a'}, 4]

copy_list[2][2] = 'b'
print(my_list)  # [1, 2, {1: 'a'}]
'''
import pickle
import copy

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

def copy_class_person(person):
    return copy.copy(person)

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

def copy_class_contacts(contacts):
    return copy.deepcopy(contacts)

# Example code:

person = Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False)
contacts = Contacts("contacts.dat", [person])

copy_contacts = copy_class_contacts(contacts)

print(copy_contacts == contacts)       # True
print(copy_contacts.contacts[0] == contacts.contacts[0])  # True
print(copy_contacts.contacts[0] is contacts.contacts[0])  # False
