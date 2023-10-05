class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact.name}")

    def view_contact_details(self, index):
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            print(contact)
        else:
            print("Invalid contact index.")

    def edit_contact(self, index, new_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = new_contact
            print(f"Contact '{new_contact.name}' updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
