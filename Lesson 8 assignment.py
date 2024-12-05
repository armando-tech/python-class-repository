import csv

# main function
def main():

    print("Welcome to the Contact Manager App")
    
    filename = "contacts.csv"
    while True:
        print("\n1. Create new contact file")
        print("2. Add new contact")
        print("3. View contacts")
        print("4. Modify a contact")
        print("5. Save and Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_csv_file(filename)
        elif choice == '2':
            add_contact(filename)
        elif choice == '3':
            view_contacts(filename)
        elif choice == '4':
            edit_contact(filename)
        elif choice == '5':
            print("See you later!")
            break
        else:
            print("Invalid option. Try again.")


# creating csv file name, phone, and email
def create_csv_file(filename):
   
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone', 'Email'])
    print("File was created successfully.")


# Add a new contact function
def add_contact(filename):
    
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone: ")
    email = input("Enter the contact's email: ")
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    print("Contact was added successfully.")

# View contact function
def view_contacts(filename):
    
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            print("\nContacts:")
            for row in reader:
                print(f"{row[0]}, {row[1]}, {row[2]}")
    except FileNotFoundError:
        print("File don't exist. Create it first.")



# Editing contact function
def edit_contact(filename):
   
    try:
        with open(filename, mode='r') as file:
            rows = list(csv.reader(file))

        print("\nCurrent Contacts:")
        for i, row in enumerate(rows):
            print(f"{i}: {row}")

        choice = int(input("Enter the number of the contact to edit: "))
        if 0 <= choice < len(rows):
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")
            rows[choice][1] = new_phone
            rows[choice][2] = new_email

            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Contact updated successfully.")
        else:
            print("Invalid choice.")
    except FileNotFoundError:
        print("File does not exist. Create it first.")
    except Exception:
        print("Something went wrong. Try again.")




if __name__ == "__main__":
    main()

    print("\nCompleted by, Armando Gaona")