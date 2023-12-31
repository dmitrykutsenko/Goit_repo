'''
Реалізуйте метод __copy__ для класу Person.

Реалізуйте методи __copy__ та __deepcopy__ для класу Contacts.
'''
import copy
import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        # Creating a new instance of Person with the same attributes
        return Person(self.name, self.email, self.phone, self.favorite)

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

    def __copy__(self):
        # Creating a new instance of Contacts with a shallow copy of the contacts list
        return Contacts(self.filename, copy.copy(self.contacts))

    def __deepcopy__(self, memo):
        # Creating a new instance of Contacts with a deep copy of the contacts list
        return Contacts(self.filename, copy.deepcopy(self.contacts, memo))

# Example usage:

person = Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", False)
contacts = Contacts("contacts.dat", [person])

# Using __copy__ method
copy_person = copy.copy(person)
copy_contacts = copy.copy(contacts)

# Using __deepcopy__ method
deepcopy_contacts = copy.deepcopy(contacts)
