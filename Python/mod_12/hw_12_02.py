'''
Є список, кожен елемент якого є словником з контактами користувача наступного виду:

{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакету json 
та зберігання отриманих даних у текстовому файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. 
Вона зберігає вказаний список у файл, використовуючи метод dump пакету json.

Структура json файлу має бути такою:

{
  "contacts": [
    {
      "name": "Allen Raymond",
      "email": "nulla.ante@vestibul.co.uk",
      "phone": "(992) 914-3792",
      "favorite": false
    },
    ...
  ]
}

Тобто список контактів повинен зберігатися за ключем "contacts", а не просто зберегти список у файл.

Друга функція read_contacts_from_file читає та повертає зазначений список contacts з файлу filename, 
збереженого раніше функцією write_contacts_to_file, використовуючи метод load пакету json.
'''

import json

def write_contacts_to_file(filename, contacts):
    data = {"contacts": contacts}
    with open(filename, 'w') as file:
        json.dump(data, file)

def read_contacts_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get("contacts", [])
    except FileNotFoundError:
        return []

# Example usage:
contacts_list = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    # Add more contacts as needed
]

# Write contacts to file
write_contacts_to_file('contacts.json', contacts_list)

# Read contacts from file
read_contacts = read_contacts_from_file('contacts.json')

# Print the read contacts
print(read_contacts)
