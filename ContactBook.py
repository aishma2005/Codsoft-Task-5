# Contact class to represent each contact
class Contacts:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"

# AddressBook class to manage contacts
class Address_Book:
    def __init__(self):
        self.contacts = []

    # Function to add a new contact
    def add_contacts(self, contact):
        self.contacts.append(contact)
        print(f"\nContact '{contact.name}' added successfully.")

    # Function to view all contacts
    def display_contacts(self):
        if self.contacts:
            print("\n===== Contact List =====")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name} - {contact.phone_number}")
            print("=========================")
        else:
            print("\nNo contacts found.")

    # Function to search for a contact by name or phone number
    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                results.append(contact)
        
        if results:
            print(f"\n===== Search Results for '{query}' =====")
            for result in results:
                print(result)
        else:
            print(f"\nNo contacts found matching '{query}'.")

    # Function to update a contact
    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"\nUpdating contact '{contact.name}':")
                new_phone = input("Enter new phone number (press Enter to keep current): ").strip()
                new_email = input("Enter new email (press Enter to keep current): ").strip()
                new_address = input("Enter new address (press Enter to keep current): ").strip()
                
                if new_phone:
                    contact.phone_number = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                
                print(f"Contact '{contact.name}' updated successfully.")
                return
        
        print(f"\nContact '{name}' not found.")

    # Function to delete a contact
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"\nContact '{contact.name}' deleted successfully.")
                return
        
        print(f"\nContact '{name}' not found.")

# Function to display the menu options
def display_menu():
    print("Address Book")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")
     

# Main function to run the address book
address_book = Address_Book()
    
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
        
    if choice == '1':
        print("Add New Contact")
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        new_contact = Contacts(name, phone_number, email, address)
        address_book.add_contacts(new_contact)
        
    elif choice == '2':
        address_book.display_contacts()
        
    elif choice == '3':
        print("Search Contact")
        query = input("Enter name or phone number to search: ")
        address_book.search_contacts(query)
        
    elif choice == '4':
        print("Update Contact")
        name = input("Enter name of contact to update: ")
        address_book.update_contact(name)
        
    elif choice == '5':
        print("Delete Contact")
        name = input("Enter name of contact to delete: ")
        address_book.delete_contact(name)
        
    elif choice == '6':
        print("\nExiting Address Book")
        break
        
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")