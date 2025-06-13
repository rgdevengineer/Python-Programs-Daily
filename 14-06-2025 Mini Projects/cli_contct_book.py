
# CLI Contact Book

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added!")

def view_contacts():
    for name, info in contacts.items():
        print(f"{name} → Phone: {info['phone']}, Email: {info['email']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Found: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Deleted.")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("New phone: ")
        email = input("New email: ")
        contacts[name] = {"phone": phone, "email": email}
        print("Updated.")
    else:
        print("Contact not found.")

def menu():
    while True:
        print("\nContact Book:\n1. Add\n2. View\n3. Search\n4. Delete\n5. Update\n6. Exit")
        choice = input("Choose: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            update_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

menu()
