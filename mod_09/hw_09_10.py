'''
Є список contacts, елементи якого - словники контактів наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

Словник містить ім'я користувача, його email, телефонний номер та властивість - обраний контакт чи ні.

Створіть функцію get_favorites(contacts), яка повертатиме список, який містить лише обрані контакти. Використовуйте при цьому функцію filter, щоб відфільтрувати по полю favorite лише обрані контакти.

'''

def get_favorites(contacts):
    # Use filter to keep only favorite contacts
    favorite_contacts = list(filter(lambda contact: contact["favorite"], contacts))
    return favorite_contacts

# Example usage:
contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "(123) 456-7890",
        "favorite": True,
    },
    # Add more contacts as needed
]

result = get_favorites(contacts)

print(result)
