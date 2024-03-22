'''
Завершуємо функціональність класу Contacts. 
На цьому етапі ми додамо до класу метод remove_contacts. 
Метод винен видаляти контакт по унікальному id у списку contacts. 
Якщо словника із зазначеним id у списку contacts не знайдено, метод жодних дій над списком contacts не робить.

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

    def remove_contact(self, contact_id):
        for contact in self.contacts:
            if contact["id"] == contact_id:
                self.contacts.remove(contact)
                break

    def remove_contacts(self, contact_ids):
        if isinstance(contact_ids, int):
            contact_ids = [contact_ids]

        self.contacts = [contact for contact in self.contacts if contact["id"] not in contact_ids]

# Example usage:

# Do not instantiate the class directly
# Instead, use the class methods through a class instance

# Create a class instance (don't do this in your code, just for demonstration)
contacts_instance = Contacts()

# Add contacts using the add_contacts method
contacts_instance.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
contacts_instance.add_contacts("John Doe", "(123) 456-7890", "john.doe@example.com", False)
contacts_instance.add_contacts("Jane Smith", "(555) 123-4567", "jane.smith@example.com", True)

# List the contacts using the list_contacts method
all_contacts = contacts_instance.list_contacts()
print("All Contacts:", all_contacts)

# Remove contacts by ids using the remove_contacts method
contacts_to_remove = [1, 3]
contacts_instance.remove_contacts(contacts_to_remove)

# List the contacts after removal
updated_contacts = contacts_instance.list_contacts()
print("Updated Contacts:", updated_contacts)
