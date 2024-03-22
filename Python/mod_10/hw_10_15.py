'''
Продовжуємо розширювати функціональність класу Contacts. 
На цьому етапі ми додамо до класу метод get_contact_by_id. 
Метод повинен шукати контакт по унікальному id у списку contacts та повертати словник з нього із зазначеним ключем id. 
Якщо словника із зазначеним id у списку contacts не знайдено, метод повертає None.

Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.
'''

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        new_contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        Contacts.current_id += 1
        self.contacts.append(new_contact)

    def get_contact_by_id(self, contact_id):
        for contact in self.contacts:
            if contact["id"] == contact_id:
                return contact
        return None

# Example usage:

# Do not instantiate the class directly
# Instead, use the class methods through a class instance

# Create a class instance (don't do this in your code, just for demonstration)
contacts_instance = Contacts()

# Add contacts using the add_contacts method
contacts_instance.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
contacts_instance.add_contacts("John Doe", "(123) 456-7890", "john.doe@example.com", False)

# List the contacts using the list_contacts method
all_contacts = contacts_instance.list_contacts()
print(all_contacts)

# Get a contact by id using the get_contact_by_id method
contact_id_to_find = 1
found_contact = contacts_instance.get_contact_by_id(contact_id_to_find)
if found_contact:
    print(f"Contact with id {contact_id_to_find}: {found_contact}")
else:
    print(f"No contact found with id {contact_id_to_find}")

