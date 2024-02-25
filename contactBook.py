def create_a_contact(name, phone_number):
    return {
        "name": name,
        "phone_number": phone_number,
    }

def add_a_contact():
    name = input("Enter new contact name: ")
    phone_number = input("Enter new phone number: ")
    contact = create_a_contact(name, phone_number)
    contacts.append(contact)
    print(f"Contact {name} added successfully!")

def search_contacts():
    search_term = input("Enter search term: ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term.lower() in contact["phone_number"].lower():
            found_contacts.append(contact)
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone_number']}")
        print(f"Found {len(found_contacts)} contacts!")
    else:
        print("No contacts found")

def delete_a_contact():
    name = input("Enter name of contact to delete: ")
    found = False
    for i, contact in enumerate(contacts):
        if contact["name"] == name:
            found = True
            del contacts[i]
            print(f"Contact {name} deleted successfully!")
            break
    if not found:
        print("Contact not found")

def list_all_the_contacts():
    if not contacts:
        print("Your contact book is empty!")
        return
    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone_number']}")

contacts = []

while True:
    print("\nContact Book Menu:")
    print("1. Add a contact")
    print("2. Search contacts")
    print("3. Delete a contact")
    print("4. List all the contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_a_contact()
    elif choice == "2":
        search_contacts()
    elif choice == "3":
        delete_a_contact()
    elif choice == "4":
        list_all_the_contacts()
    elif choice == "5":
        break
    else:
        print("Invalid choice")