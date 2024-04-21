from prettytable import PrettyTable

class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append({'Name': name, 'Phone': phone})

    def display_contacts(self):
        if not self.contacts:
            print("Phonebook is empty.")
            return
        
        table = PrettyTable()
        table.field_names = ['Name', 'Phone']
        for contact in self.contacts:
            table.add_row([contact['Name'], contact['Phone']])
        print(table)

def main():
    phonebook = Phonebook()
    
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            phonebook.add_contact(name, phone)
            print("Contact added successfully.")
        elif choice == '2':
            phonebook.display_contacts()
        elif choice == '3':
            print("Exiting phonebook.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
