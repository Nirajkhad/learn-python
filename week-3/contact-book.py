"""
This is a basic contact book program.

What this program will do:
1. Find a contact by name.
2. Add a new contact.
3. Edit a contact.
4. Delete a contact.

How to use:
1. Run the program.
2. Choose an option from the menu.
"""
ENTER_NAME_PROMPT = "Enter name: "

def display_menu():
    print("\n===== Contact Book =====")
    print("1. Find a contact")
    print("2. Add a contact")
    print("3. Edit a contact")
    print("4. Delete a contact")
    print("5. Exit")

def find_contact(contacts, name):
    if contact_not_found(contacts, name):
        return
    print(f"{name}: {contacts[name]}")

def add_contact(contacts, name, number):
    contacts[name] = number
    print("Contact added successfully!")

def edit_contact(contacts, name, number):
    if contact_not_found(contacts, name):
        return
    contacts[name] = number
    print("Contact edited successfully!")

def delete_contact(contacts, name):
    if contact_not_found(contacts, name):
        return
    del contacts[name]
    print("Contact deleted successfully!")

def contact_not_found(contacts, name):
    if name not in contacts:
        print("Contact not found!")
        return True
    return False

contacts = {}

display_menu()
while True:
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            name = input(ENTER_NAME_PROMPT)
            find_contact(contacts, name)
        case "2":
            name = input(ENTER_NAME_PROMPT)
            number = input("Enter number: ")
            add_contact(contacts, name, number)
        case "3":
            name = input(ENTER_NAME_PROMPT)
            number = input("Enter new number: ")
            edit_contact(contacts, name, number)
        case "4":
            name = input(ENTER_NAME_PROMPT)
            delete_contact(contacts, name)
        case "5":
            print("Exiting Contact Book. Goodbye!")
            break
        case _:
            print("Invalid choice")
