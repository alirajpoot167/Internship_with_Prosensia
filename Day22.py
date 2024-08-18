# Initialize an empty list to store contacts
contacts = []

def add_contact(name, phone_number):
    """
    Add a new contact to the contact book.

    Args:
        name (str): The name of the contact.
        phone_number (str): The phone number of the contact.

    Returns:
        None
    """
    # Check if the contact already exists
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print("Contact already exists.")
            return

    # Add the new contact to the list
    contacts.append((name, phone_number))
    print("Contact added successfully.")

def search_contact(name):
    """
    Search for a contact by name.

    Args:
        name (str): The name of the contact to search for.

    Returns:
        None
    """
    # Iterate through the contacts and search for the name
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print(f"Name: {contact[0]}, Phone Number: {contact[1]}")
            return

    # If the contact is not found
    print("Contact not found.")

def display_contacts():
    """
    Display all contacts in the contact book.

    Returns:
        None
    """
    # Check if the contact book is empty
    if not contacts:
        print("Contact book is empty.")
        return

    # Display all contacts
    for contact in contacts:
        print(f"Name: {contact[0]}, Phone Number: {contact[1]}")

def main():
    """
    The main function to manage the flow of the program.

    Returns:
        None
    """
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            add_contact(name, phone_number)
        elif choice == "2":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "3":
            display_contacts()
        elif choice == "4":
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()