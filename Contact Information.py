contact_list = {}

def display_contact_list():
    if not contact_list:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        print("Name\t\tPhone Number\t\tEmail\t\tAddress")
        for name, details in contact_list.items():
            phone = details['phone']
            email = details['email']
            address = details['address']
            print("{}\t\t{}\t\t{}\t\t{}".format(name, phone, email, address))

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contact_list[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added successfully.")

def search_contact():
    search_term = input("Enter a name or phone number to search: ")
    found = False
    for name, details in contact_list.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print("Name: {}\nPhone: {}\nEmail: {}\nAddress: {}".format(name, details['phone'], details['email'], details['address']))
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contact_list:
        print("Current Details:")
        print("Phone: {}\nEmail: {}\nAddress: {}".format(contact_list[name]['phone'], contact_list[name]['email'], contact_list[name]['address']))
        phone = input("Enter the new phone number (or press Enter to keep the current one): ")
        email = input("Enter the new email (or press Enter to keep the current one): ")
        address = input("Enter the new address (or press Enter to keep the current one): ")
        if phone:
            contact_list[name]['phone'] = phone
        if email:
            contact_list[name]['email'] = email
        if address:
            contact_list[name]['address'] = address
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contact_list:
        confirm = input("Are you sure you want to delete this contact? (yes/no): ")
        if confirm.lower() == "yes":
            del contact_list[name]
            print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contact_list()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thank you for using the Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()