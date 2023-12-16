'''
import csv

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "phone", "favorite"])
        writer.writeheader()
        writer.writerows(contacts)

def read_contacts_from_file(filename):
    contacts = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["favorite"] = row["favorite"].lower() == 'true'
            contacts.append(row)
    return contacts

# Example usage:
contacts_list = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    # Add more contacts as needed
]

# Write contacts to CSV file
write_contacts_to_file('contacts.csv', contacts_list)

# Read contacts from CSV file
read_contacts = read_contacts_from_file('contacts.csv')

# Print the read contacts
print(read_contacts)
'''

import csv

def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "phone", "favorite"])
        writer.writeheader()
        writer.writerows(contacts)

def read_contacts_from_file(filename):
    contacts = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["favorite"] = row["favorite"].lower() == 'true'
            contacts.append(row)
    return contacts

# Example usage:
contacts_list = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    # Add more contacts as needed
]

# Write contacts to CSV file
write_contacts_to_file('contacts.csv', contacts_list)

# Read contacts from CSV file
read_contacts = read_contacts_from_file('contacts.csv')

# Print the read contacts
print(read_contacts)
